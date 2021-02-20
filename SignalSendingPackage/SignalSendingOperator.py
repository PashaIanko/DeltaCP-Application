from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from abc import abstractmethod
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from threading import Thread
from SignalSendingPackage.SignalTimer import SignalTimer
from SignalGenerationPackage.SignalData import SignalData
from LoggersConfig import loggers


class SignalSendingOperator(CallBackOperator):
    def __init__(self, signal_main_window, plot_widget, DebugMode=True):
        super().__init__()

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

        self.FunctionWasCalled = False
        self.SendingThreadWasLaunched = False
        self.SignalVisualizerConstructed = False
        self.SendingOnPause = False
        self.SendingStopped = False
        self.EndlessSendingEnabled = False
        self.CycleSendingEnabled = True  # Предустановлено на интерфейсе
        self.CycleFinishedSuccessfully = False

        self.SendingThread = None
        self.SignalVisualizer = None
        self.PointsIterator = 0  # Just Counter to iterate over [x, y] arrays of SignalData

        self.CycleGap = 1.0  # Сколько секунд ожидать перед отправкой следующего цикла? (При непрерывной отправке)
        self.CommandExecutionTime = 0.23  # Часть времени уходит на исполнение команды (отправку частоты на
                                            # частотник, обновление отрисовки). Надо подобрать этот параметр,
                                            # и начинать исполнение команды на dt раньше, чтобы учесть задержку по времени
                                            # на исполнение команды


    @abstractmethod
    def ExecuteSending(self, Time):
        pass

    def get_start_button(self):
        return self.signal_main_window.get_start_button()

    def get_pause_radio_button(self):
        return self.signal_main_window.get_pause_radio_button()

    def get_resume_radio_button(self):
        return self.signal_main_window.get_resume_radio_button()

    def get_stop_button(self):
        return self.signal_main_window.get_stop_button()

    def get_endless_send_checkbox(self):
        return self.signal_main_window.get_endless_send_checkbox()

    def get_cycles_number_widget(self):
        return self.signal_main_window.get_cycles_number_widget()

    def get_cycle_send_checkbox(self):
        return self.signal_main_window.get_cycle_send_checkbox()

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        # Абстрактные методы, т.к. названия виджетов могут отличаться
        # для разных окошек сигналов
        StartButton = self.get_start_button()
        PauseRadioButton = self.get_pause_radio_button()
        ResumeRadioButton = self.get_resume_radio_button()
        StopButton = self.get_stop_button()
        EndlessSendCheckbox = self.get_endless_send_checkbox()

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
        EndlessSendradioButton = self.get_endless_send_checkbox()
        CycleSendradioButton = self.get_cycle_send_checkbox()

        endless_selected = EndlessSendradioButton.isChecked()
        cycle_send_selected = CycleSendradioButton.isChecked()

        self.EndlessSendingEnabled = endless_selected
        self.CycleSendingEnabled = cycle_send_selected
        loggers['Debug'].debug(f'if Endless: {self.EndlessSendingEnabled},'
                               f'if CycleSend: {self.CycleSendingEnabled}')


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
        loggers['Debug'].debug(f'SignalSendingOperator: StopSendingSignal: Setting freq = 0 & sending stop')
        self.DeltaCPClient.SetFrequency(0)
        self.DeltaCPClient.SendStop()
        self.SendingStopped = True

        loggers['Debug'].debug(f'Stopping sending thread')
        if not (self.SendingThread is None):
            self.SendingThread.join()
            self.SendingThread = None

        # Отрисуем на графике исходный сигнал
        self.SignalVisualizer.ResetPlot()
        # Закроем окошко с визуализацией
        # if not (self.SignalVisualizer.check_if_window_closed()):
        #    self.SignalVisualizer.close_visualization_window()

    def TestTimer(self):
        # Перед отправкой частоты по прерыванию, необходимо проверить - а не закрыл ли пользователь
        # окошко с визуализацией. Если закрыл - то мы ничего уже не отправляем. Тогда выставляем частоту 0Гц
        # SetFrequency(0) и посылаем STOP

        window_is_closed = self.SignalVisualizer.check_if_window_closed()
        if window_is_closed:
            loggers['Application'].info(f'Visualization window was closed --> Application Stop Signal Sending')
            self.StopSendingSignal()  # TODO: Теперь окошко встроено --> Нет нужды проверять window_is_closed
        else:
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
        print(f'Restarting Visualization!!')
        self.SignalVisualizer.Restart(TimeArray)

    def LaunchSendingThread(self):
        self.SendingThread = Thread(target=self.ThreadFunc)
        self.SendingThread.start()

    def StartSendingSignal(self):

        # Сначала надо наладить частоту опроса - Это небольной костыль.

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
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        # TODO: Check that TimeFrom <= TimeTo
        Time = SignalData.x_with_requests.copy()
        updated_x = SignalData.x.copy()
        self.SignalVisualizer.RefreshData(SignalData.x, SignalData.y)
        self.ExecuteSending(Time)

        cycle_counter = 0
        cycle_number_widget = self.signal_main_window.get_cycles_number_widget()
        while True:
            if self.SendingStopped == True:
                self.SendingStopped = False  # Reset the flag
                return
            elif self.EndlessSendingEnabled and self.CycleFinishedSuccessfully:
                # Случай бесконечной отправки
                # update Time array and restart the cycle
                self.CycleFinishedSuccessfully = False
                self.RestartSending(Time, updated_x)

            elif self.CycleSendingEnabled and self.CycleFinishedSuccessfully:
                # Случай отправки N циклов
                cycle_counter += 1
                cycles_to_perform = cycle_number_widget.value()
                if cycle_counter >= cycles_to_perform:
                    return
                else:
                    self.CycleFinishedSuccessfully = False
                    self.RestartSending(Time, updated_x)

    def RestartSending(self, Time, updated_x):
        upd_val = SignalData.x[-1]
        Time = self.update_time_array(Time, upd_val)
        updated_x = self.update_time_array(updated_x, upd_val)

        # restarting points Iterator, Visualisation and Sending Thread
        self.PointsIterator = 0
        self.SignalVisualizer.Restart(updated_x)  # SignalVisuzlizer отрисовывает X, Y, без реквестов
        self.ExecuteSending(Time)

    @staticmethod
    def update_time_array(arr, upd_val):
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

