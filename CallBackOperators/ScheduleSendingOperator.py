from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from LoggersConfig import loggers
from DeltaCPRegisters import DeltaCPRegisters
import datetime
from threading import Thread
import time
from SignalGenerationPackage.Point import Point
from queue import Queue


class ScheduleSendingOperator(SignalSendingOperator):

    # ScheduleSendingOperator - для отправки сигнала-"лесенки",
    # из модуля "Расписание Эксперимента"

    def __init__(self, signal_main_window, plot_widget, model, DebugMode, SendRetry):
        super().__init__(signal_main_window, plot_widget, DebugMode)

        self.current_point = None
        self.model = model
        #self.FreqSendingTime = 0.0  # Поправка 1 сек на отправку частоты

        self.CurrentFreq = None
        self.SetFreq = None
        self.tasks_queue = Queue()

        self.SendRetry = SendRetry

        self.AccelerationTime = 20  # За 20 сек от F_min до F_max  # TODO: На интерфейс эти параметры выставить
        self.DecelerationTime = 20  # За 20 сек от F_min до F_max

        self.RetryAccuracy = 0.5  # Если изменение следующей опрошенной частоты

        self._set_frequency = False
        self._requested_frequency = False
        # менее чем на self.RetryAccuracy, то повторяем опрос

        # Model (модель) нужна, для того чтобы перед отправкой пересчитать необходимые времёна
        # разгона / замедления

        # На первом цикле исполнение - самую первую частоту задаём и ожидаем, пока не
        # достигнем её. Например, если первое значение = 30 Гц. Зададим и подождём, пока частотник достигнет
        # её. Только после этого продолжаем отправку.

    def SetFrequency(self, val_to_set):
        t_before_write = time.time()
        self.DeltaCPClient.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister, val_to_set)
        self.SendingLogger.log_send_dt(time.time() - t_before_write)

    def SendRequestMonitor(self):
        while True:
            if self.SendingStopped or self.wait_to_finish:
                return
            elif not self.tasks_queue.empty():
                # Значит есть задача на отправку / запрос
                pt = self.tasks_queue.get()

                if pt.to_send:
                    self.SetFrequency(int(pt.y * 100))
                    self.SetFreq = pt.y
                    self.SignalVisualizer.UpdateSetFrequency(pt.x, pt.y)
                    self.setup_set_flag()
                else:
                    # Значит опрашиваем
                    t_before_request = time.time()
                    self.CurrentFreq = self.DeltaCPClient.ReadRegister(DeltaCPRegisters.CurrentFrequencyRegister, self.DebugMode)
                    self.SendingLogger.log_request_dt(time.time() - t_before_request)
                    self.setup_request_flag()
                    if self.CurrentFreq is not None:
                        self.CurrentFreq /= 100

                        if self.SendRetry:
                            # На случай, если команда задания частоты не прошла,
                            # необходимо повторять отправку до тех пор, пока
                            # опрошенная частота не начнёт отличаться от LowLevelFrequency
                            # или HighLevelFrequency (в зависимости от того, что мы неуспешно
                            # попытались задать)
                            self.RetrySending(pt)
                    self.SendingLogger.log(f_expect=pt.y, f_real=self.CurrentFreq,
                                           t_expect=pt.x,
                                           t_real=datetime.datetime.now().time())
                    self.SignalVisualizer.UpdateCurrentFrequency(pt.x, self.CurrentFreq)

    def setup_set_flag(self):
        self._set_frequency = True
        self._requested_frequency = False  # Взаимоисключающие

    def setup_request_flag(self):
        self._set_frequency = False
        self._requested_frequency = True  # Взаимоисключающие

    def RetrySending(self, point):
        set_freq = self.SetFreq
        if self._requested_frequency and abs(self.CurrentFreq - set_freq) <= self.RetryAccuracy:
            self.SetFrequency(set_freq)  # перезадаём последнюю заданную частоту
            self.SignalVisualizer.UpdateSetFrequency(point.x, self.model.HighLevelFrequency)

    # Переопределённый метод, т.к. немного отличается (Надо задать t_разгона, t_замедления перед отправкой)
    def StartSendingSignal(self):

        if not self.task_queue_thread_started:
            self.task_queue_thread = Thread(target=self.SendRequestMonitor)
            self.task_queue_thread.start()
            self.task_queue_thread_started = True

        # Раз готовы к старту - тогда отправляем на частотник
        # необходимые времёна разгона
        self.SendingLogger.start_database()
        self.DeltaCPClient.SetAccelerationTime1(self.AccelerationTime)  # TODO: Взять время с GUI и выставить его, заданное пользователем
        self.DeltaCPClient.SetDecelerationTime1(self.DecelerationTime)  # TODO: Взять время с GUI и выставить его, заданное пользователем


        current_cycle_display = self.signal_main_window.get_LCD_display()
        current_cycle_display.display(0)  # Сбросить значение на дисплее текущего цикла

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

    # overridden
    def ExecuteSending(self, point_arr):

        points = point_arr
        DeltaTimes = SignalData.dx
        Dts_len = len(DeltaTimes)


        self.FunctionWasCalled = False  # Line is important! For multithreading

        if self.IsFirstCycle:
            self.PointsIterator = 0
        else:
            self.PointsIterator = 1
        self.current_point = points[self.PointsIterator]


        # На первом прогоне надо предварительно выставить начальную частоту
        if self.IsFirstCycle == True:
            preset_value = self.model.frequencies[0]
            self.IsFirstCycle = False
            self.PresetFrequency(preset_value)
            self.setup_set_flag()  # Задали самую первую частоту -> выставили флаги
            self.CurrentFreq = preset_value
            self.start_sending_time = time.time()


        # После выставления начальной частоты - Ждём cycle gap и выставляем следующую точку
        if self.Timer.if_started == True:  # Если уже дали старт таймеру на предудущем цикле
            self.Timer.reset(self.CycleGap)
        else:
            self.Timer.interval = self.CycleGap
            self.Timer.run()

        # После этого - ждём delta_t[i] и выставляем следующие точки, i = 0, 1, ...
        if Dts_len != 0:  # If the Time array has only one point, then we've already accomplished it in
                          # the method self.Timer.run()

            self.PointsIterator = 1
            while self.PointsIterator <= Dts_len:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False
                    self.current_point = points[self.PointsIterator]

                    if self.CycleRestarted:
                        self.CycleRestarted = False
                    dt_to_wait = max(0.01, DeltaTimes[self.PointsIterator - 1] -
                                     self.CommandExecutionTime - self.lag_portion)

                    self.Timer.reset(dt_to_wait)
                    self.PointsIterator += 1

                if self.SendingStopped:
                    return

        while True:  # Дожидаемся отправки последней команды (на краю сэмпла, чтобы на визуализации тоже это увидеть)
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                return

    def TestTimer(self):
        t0 = time.time()
        if not self.SendingStopped:
            current_point = self.current_point
            self.tasks_queue.put(Point(x=current_point.x, y=current_point.y, to_send=current_point.to_send))
        self.CommandExecutionTime = time.time() - t0
        self.FunctionWasCalled = True

    # overridden
    def value_changed(self, val):
        pass  # You dont need these methods for the logic of this class

    # overridden
    def init_slider(self):
        pass # You dont need these methods for the logic of this class

    # overridden
    def init_line_edit(self):
        pass # You dont need these methods for the logic of this class
