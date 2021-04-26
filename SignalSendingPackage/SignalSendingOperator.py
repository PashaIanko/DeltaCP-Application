from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from abc import abstractmethod
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from threading import Thread
from SignalSendingPackage.SignalTimer import SignalTimer
from SignalGenerationPackage.SignalData import SignalData
from LoggersConfig import loggers
from SignalSendingPackage.SendingLogger import SendingLogger
from time import sleep, time
import copy


class SignalSendingOperator(CallBackOperator):
    def __init__(self, signal_main_window, plot_widget, DebugMode=True):
        super().__init__(signal_main_window, model=None, value_range=None)

        # Поскольку виджеты для отправки сигнала находятся на окошке
        # для генерации сигнала (user_interface), названия
        # виджетов могут отличаться (Название самих классов).
        # Поэтому надо их переопределить
        self.signal_main_window = signal_main_window
        self.plot_widget = plot_widget

        self.DebugMode = DebugMode
        # Ниже - Набор параметров для обоих способов отправки сигнала -
        # наперёд (Как Сергей сказал), и более наивный способ
        self.TimeStamp = 0
        self.ValueToSend = 0
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        self.DeltaCPClient = DeltaCPClient()
        self.SendingLogger = SendingLogger()

        self.FunctionWasCalled = False
        self.SendingThreadWasLaunched = False
        self.SignalVisualizerConstructed = False
        self.SendingOnPause = False
        self.SendingStopped = False
        self.EndlessSendingEnabled = False
        self.CycleSendingEnabled = True  # Предустановлено на интерфейсе
        self.CycleFinishedSuccessfully = False
        self.CycleRestarted = False
        self.IsFirstCycle = True

        self.SendingThread = None
        self.SignalVisualizer = None
        self.PointsIterator = 0  # Just Counter to iterate over [x, y] arrays of SignalData

        self.CycleGap = 0.01  # Сколько секунд ожидать перед отправкой следующего цикла? (При непрерывной отправке)
        self.CommandExecutionTime = 0.0  # Часть времени уходит на исполнение команды (отправку частоты на
        # частотник, обновление отрисовки). Надо подобрать этот параметр,
        # и начинать исполнение команды на dt раньше, чтобы учесть задержку по времени
        # на исполнение команды
        self.tasks_queue = None
        self.task_queue_thread = None  # Параллельный поток, мониторящий очередь задач
        self.wait_to_finish = False
        self.task_queue_thread_started = False

        self.lag_portion = 0  # Отправку каждой команды в следующем цикле делаем на lag_portion быстрее, компенсируя задержки по времени
        self.start_sending_time = 0
        self.cycle_counter = 0

        self.point_arr = None  # Массив точек для отправки. Изначально это копия SignalData.point_array_with_requests,
        # далее он пересчитывается с каждым циклом

    @abstractmethod
    def ExecuteSending(self, Time):
        pass

    def get_log_filename_lineedit(self):
        return self.signal_main_window.get_log_filename_lineedit()

    def get_start_button(self):
        return self.signal_main_window.get_start_button()

    def get_pause_radio_button(self):
        return self.signal_main_window.get_pause_radio_button()

    def get_resume_radio_button(self):
        return self.signal_main_window.get_resume_radio_button()

    def get_stop_button(self):
        return self.signal_main_window.get_stop_button()

    def get_endless_send_radiobutton(self):
        return self.signal_main_window.get_endless_send_radiobutton()

    def get_cycles_number_widget(self):
        return self.signal_main_window.get_cycles_number_widget()

    def get_cycle_send_radiobutton(self):
        return self.signal_main_window.get_cycle_send_radiobutton()

    # overridden
    def ConnectCallBack(self):

        # Абстрактные методы, т.к. названия виджетов могут отличаться
        # для разных окошек сигналов
        StartButton = self.get_start_button()
        PauseRadioButton = self.get_pause_radio_button()
        ResumeRadioButton = self.get_resume_radio_button()
        StopButton = self.get_stop_button()
        EndlessSendCheckbox = self.get_endless_send_radiobutton()

        # Надо сделать так, чтобы бесконечная отправка (EndlessSendCheckbox)
        # И отправка циклов (CyclesNumberSpinBox) были взаимоисключающими
        # Поэтому, коннектим взаимоисключающие отклики
        EndlessSendCheckbox.toggled.connect(lambda: self.EnableSendingRegime())  # Какой режим - бесконечной отправки
        # Или кол-во циклов

        StartButton.clicked.connect(self.StartSendingSignal)
        PauseRadioButton.toggled.connect(self.PauseSending)
        ResumeRadioButton.toggled.connect(self.ResumeSending)
        StopButton.clicked.connect(self.StopSendingSignal)

    def EnableSendingRegime(self):
        EndlessSendradioButton = self.get_endless_send_radiobutton()
        CycleSendradioButton = self.get_cycle_send_radiobutton()

        endless_selected = EndlessSendradioButton.isChecked()
        cycle_send_selected = CycleSendradioButton.isChecked()

        self.EndlessSendingEnabled = endless_selected
        self.CycleSendingEnabled = cycle_send_selected

    def PauseSending(self):
        if self.window.PauseSendingradioButton.isChecked():
            loggers['Application'].info('Sending Paused')
            loggers['SignalSending'].info('Sending Paused')

            self.SendingOnPause = True
            self.window.ResumeSendingradioButton.setChecked(False)
        else:
            self.window.ResumeSendingradioButton.setChecked(True)

    def ResumeSending(self):
        if self.window.ResumeSendingradioButton.isChecked():
            loggers['Application'].info('Sending Paused')
            loggers['SignalSending'].info('Sending Paused')

            self.SendingOnPause = False
            self.window.PauseSendingradioButton.setChecked(False)
        else:
            self.window.PauseSendingradioButton.setChecked(True)

    def StopSendingSignal(self):
        try:
            self.SendingStopped = True
            if self.task_queue_thread is not None:
                self.wait_to_finish = True
                self.task_queue_thread.join()
                self.wait_to_finish = False
                self.task_queue_thread_started = False  # дождались завершения параллельного потока с помощью join(). Тред убился. Поэтому
                                                        # выставляем флаг, что тред не стартовал, чтобы вновь его создать при нажатии "Start Sending"
            if self.tasks_queue is not None:
                with self.tasks_queue.mutex:
                    self.tasks_queue.queue.clear()

            self.DeltaCPClient.SetFrequency(0)
            self.DeltaCPClient.SendStop()

            self.IsFirstCycle = True
            self.lag_portion = 0  # Обнуление задержек по времени

            current_cycle_display = self.signal_main_window.get_LCD_display()
            current_cycle_display.display(0)  # Обновить дисплей с текущим циклом - обратно на ноль

            loggers['Debug'].debug(f'Stopping sending thread')
            if not (self.SendingThread is None):
                self.SendingThread.join()
                self.SendingThread = None

            # Отрисуем на графике исходный сигнал
            self.SignalVisualizer.ResetPlot()

            # Сохраним файл лога
            self.SaveLog()
        except:
            import sys
            print(sys.exc_info())

    def SaveLog(self):
        log_lineedit = self.get_log_filename_lineedit()
        log_filename = log_lineedit.text()

        self.SendingLogger.output_filename = log_filename + '.xlsx'
        self.SendingLogger.save_database()

    def TestTimer(self):

        # Если self.ValueToSend - это None. Значит это "фиктивная точка" - то есть
        # не надо выставлять её на частотник. Надо только опросить текущую частоту и вывести на график.
        # Итого, опрашивать частоту надо в любом случае, поэтому вывел её за пределы if/else
        if self.DebugMode:
            CurrentFreq = 0
        else:
            CurrentFreq = self.DeltaCPClient.RequestCurrentFrequency()

        if not self.SendingStopped:
            self.SignalVisualizer.UpdateCurrentFrequency(self.TimeStamp, CurrentFreq)

            if self.ValueToSend is None:
                loggers['Debug'].debug(f'SignalSendingOperator: TestTimer: Request current freq')
                loggers['SignalSending'].info(f'Current frequency = {CurrentFreq} Hz')
            else:
                loggers['Debug'].debug(f'TestTimer: ValueToSend = {self.ValueToSend}')
                # Если окошко не закрыто - продолжаем визуализацию и отправку
                value_to_send = int(self.ValueToSend * 100)  # Привести к инту, иначе pymodbus выдаёт ошибку
                self.DeltaCPClient.SetFrequency(value_to_send)
                self.SignalVisualizer.UpdateSetFrequency(self.TimeStamp, self.ValueToSend)
        self.FunctionWasCalled = True

    def RestartSignalIterator(self):
        self.PointsIterator = 0

    def RestartVisualization(self, TimeArray):
        self.SignalVisualizer.Restart(TimeArray)

    def LaunchSendingThread(self):
        self.SendingThread = Thread(target=self.ThreadFunc)
        self.SendingThread.start()

    def StartSendingSignal(self):

        current_cycle_display = self.signal_main_window.get_LCD_display()
        current_cycle_display.display(1)  # Сбросить значение на дисплее текущего цикла

        if self.SendingThread is None:
            self.SendingStopped = False  # Надо почистить флаг - иначе неверно работает при последовательности:
            # Закрыть визуализацию - Нажать Stop - Нажать Start

            loggers['Debug'].debug(f'Launching thread, thread is None')
            if not self.SignalVisualizerConstructed:
                self.SignalVisualizer = SignalVisualizer(self.plot_widget)
            self.DeltaCPClient.SendStart()
            self.LaunchSendingThread()
        else:
            if not self.SendingThread.is_alive():
                loggers['Debug'].debug(f'Launching thread, thread is not alive')
                self.SignalVisualizer.Restart(TimeArray=[])
                self.RestartSignalIterator()
                self.SendingStopped = False  # Надо почистить этот флаг
                self.LaunchSendingThread()
            else:
                loggers['Debug'].debug(f'Prev sending thread is executing, cant launch one')

    def ThreadFunc(self):
        self.Timer = SignalTimer(interval=0.1, function=self.TestTimer)

        self.point_arr = copy.deepcopy(SignalData.point_array_with_requests)
        updated_x = SignalData.x.copy()
        self.SignalVisualizer.RefreshData(SignalData.x, SignalData.y)
        self.ExecuteSending(self.point_arr)

        self.cycle_counter = 0
        cycle_number_widget = self.signal_main_window.get_cycles_number_widget()

        current_cycle_display = self.signal_main_window.get_LCD_display()
        while True:
            if self.SendingStopped == True:
                self.SendingStopped = False  # Reset the flag
                current_cycle_display.display(0)
                return

            if self.CycleFinishedSuccessfully:
                self.CycleFinishedSuccessfully = False

                self.cycle_counter += 1

                if self.EndlessSendingEnabled:
                    current_cycle_display.display(self.cycle_counter + 1)
                    self.RestartSending(updated_x)

                if self.CycleSendingEnabled:
                    cycles_to_perform = cycle_number_widget.value()
                    if self.cycle_counter >= cycles_to_perform:
                        return
                    else:
                        current_cycle_display.display(self.cycle_counter + 1)
                        self.RestartSending(updated_x)

    def RestartSending(self, updated_x):
        upd_val = SignalData.x[-1]
        self.update_time_stamps(upd_val)
        updated_x = self.update_array(updated_x, upd_val)

        # restarting points Iterator, Visualisation and Sending Thread
        self.PointsIterator = 0
        self.SignalVisualizer.Restart(updated_x)  # SignalVisualizer отрисовывает X, Y, без реквестов

        self.CycleRestarted = True

        dt_diff = (time() - self.start_sending_time) - ((self.cycle_counter) * self.model.WholePeriod)
        self.SendingLogger.log_cycle_dt_delay(dt_diff)
        if dt_diff > 0:
            self.lag_portion = dt_diff / (len(SignalData.point_array_with_requests) - 2)
            loggers['Debug'].debug(f'lag portion = {self.lag_portion}')
        self.ExecuteSending(self.point_arr)

    def update_time_stamps(self, upd_val):
        for p in self.point_arr:
            p.x += upd_val

    @staticmethod
    def update_array(arr, upd_val):
        for i in range(len(arr)):
            arr[i] += upd_val
        return arr

    def Restart(self, Time):
        self.CycleFinishedSuccessfully = False
        upd_val = SignalData.x[-1]
        for i in range(len(Time)):
            Time[i] += upd_val + SignalData.dx[i]
        self.RestartSignalIterator()
        self.RestartVisualization(Time)
        self.ExecuteSending(Time)

    def PresetFrequency(self, value):
        # Перед запуском, если частота ненулевая - убедиться, предварительно задать требуемую начальную частоту
          # Привести к инту, иначе pymodbus выдаёт ошибку
        value_to_send = int(value * 100)
        self.DeltaCPClient.SetFrequency(value_to_send)

        if self.DebugMode:
            return
        else:
            self.RequestFreqUntilEqual(value)



    def RequestFreqUntilEqual(self, value):
        accuracy = 0.05
        dt_to_wait = 1.7  # Время, которое подождём, прежде чем опять запросить частоту, чтобы сравнить
                            # с предустановленной
        requests_limit = 4  # Может быть такое, что задание частоты (SetFrequency) не пройдёт с первого раза
                            # Тогда, спустя retries попыток опросить частоту, будем задавать её повторно
        requests_number = 0
        prev_freq = None
        value_to_send = int(value * 100)


        while True:
            sleep(dt_to_wait)
            current_freq = self.DeltaCPClient.RequestCurrentFrequency(DebugMode=self.DebugMode)
            # loggers['Debug'].debug(f'RequestFreqUntilEqual: F_current = {current_freq} Hz')

            if not (current_freq is None) and abs(current_freq - value) <= accuracy:
                return  # Значит, с точностью до accuracy уже достигли частоты

            requests_number += 1
            if requests_number == requests_limit:
                requests_number = 0
                # На случай, если предзадана большАя частота (например, 30 Гц), и разгон до неё
                # маленький - может быть ситуация, при которой команда задания частоты прошла успешно,
                # просто частотный преобразователь ещё не успел разогнаться. Тогда, задавать частоту
                # повторно имеет смысл только при current_freq == prev_freq
                if (prev_freq is not None) and (current_freq is not None):
                    loggers['Debug'].debug(f'Waiting limit reached: F_prev = {prev_freq}, F_current = {current_freq}')
                    if abs(prev_freq - current_freq) <= accuracy:  # т.е. если предыдущая частота совпадает с текущей, то задаём ещё раз
                        loggers['Debug'].debug(f'RequestFreqUntilEqual: Retrying to set frequency')
                        self.DeltaCPClient.SetFrequency(value_to_send)

            prev_freq = current_freq
            # loggers['Debug'].debug(f'RequestFreqUntilEqual: F_prev = {prev_freq} Hz')