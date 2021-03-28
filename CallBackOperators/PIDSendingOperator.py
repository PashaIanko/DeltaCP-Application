from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from PopUpNotifier.PopUpNotifier import PopUpNotifier
from LoggersConfig import loggers
from DeltaCPRegisters import DeltaCPRegisters
import datetime
from threading import Thread
import time
from SignalGenerationPackage.Point import Point
from queue import Queue


class PIDSendingOperator(SignalSendingOperator):

    # PIDSending operator работает только с EdgeSignal, т.е. с трапецией, содержащей
    # только крайние "угловые точки". Промежуточных точек нет. Суть в том, чтобы
    # по заданному пользователем ускорению/замедлению на трапеции вычислить оптимальное
    # Время разгона и замедления. Перед отправкой, эти времена разгона и замедления
    # отправляются в регистры частотного преобразователя. А дальше - мы задаём
    # целевую частоту "Наперёд". Разгон при этом регулирует сам частотный преобразователь, т.к. мы
    # уже пересчитали оптимальные времёна разгона и занесли их в регистр

    def __init__(self, signal_main_window, plot_widget, model, DebugMode):
        super().__init__(signal_main_window, plot_widget, DebugMode)

        self.current_point = None
        self.model = model
        self.FreqSendingTime = 0.0  # Поправка 1 сек на отправку частоты
        self.task_queue_thread = Thread(target=self.SendRequestMonitor)


        self._set_upper_freq = True
        self.CurrentFreq = None

        self.tasks_queue = Queue()
        self.task_queue_thread_started = False


        # Model (модель) нужна, для того чтобы перед отправкой пересчитать необходимые времёна
        # разгона / замедления

        # На первом цикле исполнение - самую первую частоту задаём и ожидаем, пока не
        # достигнем её. Например, если первое значение = 30 Гц. Зададим и подождём, пока частотник достигнет
        # её. Только после этого продолжаем отправку.


    def SendRequestMonitor(self):
        while True:
            if self.SendingStopped or self.wait_to_finish:
                return
            elif not self.tasks_queue.empty():
                # Значит есть задача на отправку / запрос
                [pt, set_upper_freq] = self.tasks_queue.get()

                if pt.to_send:
                    if set_upper_freq:
                        val_to_set = int(self.model.HighLevelFrequency * 100)
                    else:
                        val_to_set = int(self.model.LowLevelFrequency * 100)

                    t_before_write = time.time()
                    self.DeltaCPClient.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister, val_to_set)
                    self.SendingLogger.log_send_dt(time.time() - t_before_write)
                    self.SignalVisualizer.UpdateSetFrequency(pt.x, val_to_set / 100)
                else:
                    # Значит опрашиваем
                    if self.DebugMode:
                        self.CurrentFreq = 0
                    else:
                        t_before_request = time.time()
                        # self.CurrentFreq = self.DeltaCPClient.RequestCurrentFrequency()
                        self.CurrentFreq = self.DeltaCPClient.ReadRegister(DeltaCPRegisters.CurrentFrequencyRegister) / 100
                        self.SendingLogger.log_request_dt(time.time() - t_before_request)

                    self.SendingLogger.log(f_expect=pt.y, f_real=self.CurrentFreq,
                                           t_expect=pt.x,
                                           t_real=datetime.datetime.now().time())

                    self.SignalVisualizer.UpdateCurrentFrequency(pt.x, self.CurrentFreq)


    # Переопределённый метод, т.к. немного отличается (Надо задать t_разгона, t_замедления перед отправкой)
    def StartSendingSignal(self):

        # Проверим - готовы начать, или желаемое ускорение / замедление
        # превышает критическое
        necessary_t_acceleration = self.model.NecessaryAccelerationTime
        necessary_t_deceleration = self.model.NecessaryDecelerationTime
        ready_to_start = self.check_acceleration_deceleration(necessary_t_acceleration, necessary_t_deceleration)

        if not self.task_queue_thread_started:
            self.task_queue_thread_started = True
            self.task_queue_thread.start()
        if ready_to_start:
            # Раз готовы к старту - тогда отправляем на частотник
            # необходимые времёна разгона
            self.SendingLogger.start_database()
            self.DeltaCPClient.SetAccelerationTime1(necessary_t_acceleration)
            self.DeltaCPClient.SetDecelerationTime1(necessary_t_deceleration)

            loggers['Debug'].debug(f'After Preset of t_acc, t_dec: t_acc, t_dec = '
                                   f'{self.DeltaCPClient.RequestAccelerationTime1(), self.DeltaCPClient.RequestDecelerationTime1()}')

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

    def check_acceleration_deceleration(self, necessary_t_acceleration, necessary_t_deceleration):
        # Перед началом отправки, надо:
        # 1. Опросить текущие t разгона, замедления
        # 2. Понять, какие t разгона, замедления нам нужны
        # 3. Проверить - необходимые времёна в пределах критических?
        # 4. Если времёна больше критических, опросить пользователя - ОК ли продолжать отправку с
        #     требуемыми t разгона замедления?
        # 4. Если ОК, то задаём новые значения на частотник,
        #    и погнали отправлять сигнал

        # 1
        current_t_acceleration = self.DeltaCPClient.RequestAccelerationTime1()
        current_t_deceleration = self.DeltaCPClient.RequestDecelerationTime1()

        # 2
        diff_freq = abs(self.model.HighLevelFrequency - self.model.LowLevelFrequency)

        try:
            necessary_acceleration = diff_freq / necessary_t_acceleration
            necessary_deceleration = diff_freq / necessary_t_deceleration
        except ZeroDivisionError:
            PopUpNotifier.Error(f'Zero Acceleration/Deceleration time!')
            return False

        # 3
        critical_acceleration = self.model.CriticalAcceleration
        critical_deceleration = self.model.CriticalDeceleration

        if (abs(necessary_acceleration) >= abs(critical_acceleration)) or (
                abs(necessary_deceleration) >= abs(critical_deceleration)):
            user_decision = PopUpNotifier.CriticalAccelerDecelerQuestion(
                current_t_acceleration, current_t_deceleration,
                critical_acceleration, critical_deceleration,
                necessary_acceleration, necessary_deceleration
            )
            return user_decision
        else:
            return True

    # overridden
    def ExecuteSending(self):

        points = SignalData.point_array_with_requests
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
            preset_value = self.model.LowLevelFrequency
            self.IsFirstCycle = False
            self.PresetFrequency(preset_value)
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
            self.tasks_queue.put([Point(x=current_point.x, y=current_point.y, to_send=current_point.to_send), current_point.y == self.model.HighLevelFrequency])
        self.CommandExecutionTime = time.time() - t0
        self.FunctionWasCalled = True
