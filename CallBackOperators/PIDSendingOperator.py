from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from PopUpNotifier.PopUpNotifier import PopUpNotifier
from LoggersConfig import loggers
import time


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
        self.IsFirstCycle = True

        self.model = model  # Model (модель) нужна, для того чтобы перед отправкой пересчитать необходимые времёна
        # разгона / замедления

        # На первом цикле исполнение - самую первую частоту задаём и ожидаем, пока не
        # достигнем её. Например, если первое значение = 30 Гц. Зададим и подождём, пока частотник достигнет
        # её. Только после этого продолжаем отправку.


    # Переопределённый метод, т.к. немного отличается (Надо задать t_разгона, t_замедления перед отправкой)
    def StartSendingSignal(self):

        # Проверим - готовы начать, или желаемое ускорение / замедление
        # превышает критическое
        necessary_t_acceleration = self.model.NecessaryAccelerationTime
        necessary_t_deceleration = self.model.NecessaryDecelerationTime
        ready_to_start = self.check_acceleration_deceleration(necessary_t_acceleration, necessary_t_deceleration)

        if ready_to_start:
            # Раз готовы к старту - тогда отправляем на частотник
            # необходимые времёна разгона
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
    def ExecuteSending(self, Time):
        DeltaTimes = SignalData.dx_with_requests
        Dts_len = len(DeltaTimes)

        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 0
        self.TimeStamp = Time[self.PointsIterator]  # В какой момент времени на графике мы выставим ValueToSend
        self.ValueToSend = SignalData.y_with_requests[self.PointsIterator]  # Сигнал опережает теперь


        # На первом прогоне надо предварительно выставить начальную частоту
        if self.IsFirstCycle == True:
            preset_value = SignalData.y_with_requests[0]
            self.IsFirstCycle = False
            self.PresetFrequency(preset_value)

        # После выставления начальной частоты - Ждём cycle gap и выставляем следующую точку
        if self.Timer.if_started == True:  # Если уже дали старт таймеру на предудущем цикле
            self.Timer.reset(self.CycleGap)
        else:
            self.Timer.interval = self.CycleGap
            self.Timer.run()

        # После этого - ждём delta_t[i] и выставляем следующие точки, i = 0, 1, ...
        if Dts_len != 0:  # If the Time array has only one point, then we've already accomplished it in
                          # the method self.Timer.run()

            i = 0
            self.PointsIterator = 1
            while i < Dts_len:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False

                    self.ValueToSend = SignalData.y_with_requests[self.PointsIterator]
                    self.TimeStamp = Time[self.PointsIterator]
                    dt_to_wait = DeltaTimes[i] - self.CommandExecutionTime
                    loggers['SignalSending'].info(f'After dt={dt_to_wait} sec, I will send {self.ValueToSend} Hz')
                    self.Timer.reset(dt_to_wait)

                    # if i == Dts_len - 1:
                    #     # Это значит, мы достигли конца отправляемого сигнала.
                    #     # Поскольку отправляем наперёд - надо отправить начальную точку сигнала,
                    #     # При этом подождав detaT[-1] (Последний временной отрезок)
                    #     # Тогда, когда цикл отправки возобновится - начальная точка уже была отправлена в
                    #     # Этом коде. Поэтому в новом цикле начинаем отправку не с 0й, а с 1ой точки.
                    #     self.ValueToSend = SignalData.y_with_requests[0]
                    #     self.TimeStamp = Time[self.PointsIterator - 1]
                    #     loggers['SignalSending'].info(f'After dt={dt_to_wait} sec, I will send {self.ValueToSend} Hz')
                    #     self.Timer.reset(DeltaTimes[-1] - self.CommandExecutionTime)
                    #
                    # else:
                    #     self.ValueToSend = SignalData.y_with_requests[self.PointsIterator]
                    #     self.TimeStamp = Time[self.PointsIterator]
                    #     dt_to_wait = DeltaTimes[i] - self.CommandExecutionTime
                    #     loggers['SignalSending'].info(f'After dt={dt_to_wait} sec, I will send {self.ValueToSend} Hz')
                    #     self.Timer.reset(dt_to_wait)

                    i += 1
                    self.PointsIterator += 1

                if self.SendingStopped:
                    return

        while True:  # Дожидаемся отправки последней команды (на краю сэмпла, чтобы на визуализации тоже это увидеть)
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                loggers['SignalSending'].info(f'Finished Cycle')
                return

    def TestTimer(self):
        t0 = time.time()
        # Перед отправкой частоты по прерыванию, необходимо проверить - а не закрыл ли пользователь
        # окошко с визуализацией. Если закрыл - то мы ничего уже не отправляем. Тогда выставляем частоту 0Гц
        # SetFrequency(0) и посылаем STOP

        # Если self.ValueToSend - это None. Значит это "фиктивная точка" - то есть
        # не надо выставлять её на частотник. Надо только опросить текущую частоту и вывести на график.
        # Итого, опрашивать частоту надо в любом случае, поэтому вывел её за пределы if/else
        if self.DebugMode:
            CurrentFreq = 0
        else:
            CurrentFreq = self.DeltaCPClient.RequestCurrentFrequency()

        if not self.SendingStopped:

            self.SignalVisualizer.UpdateCurrentFrequency(self.TimeStamp, CurrentFreq)

            # Если поставлено на Паузу - тогда последнюю опрошенную частоту задаём и просто ждём, пока
            # флаг паузы не снимется
            if self.SendingOnPause:
                print(f'SENDING PAUSED')
                self.DeltaCPClient.SetFrequency(int(CurrentFreq * 100))
            else:
                if self.ValueToSend is not None:
                    loggers['Debug'].debug(f'TestTimer: ValueToSend = {self.ValueToSend}')
                    value_to_send = int(self.ValueToSend * 100)  # Привести к инту, иначе pymodbus выдаёт ошибку
                    self.DeltaCPClient.SetFrequency(value_to_send)
                    self.SignalVisualizer.UpdateSetFrequency(self.TimeStamp, self.ValueToSend)
        self.FunctionWasCalled = True

        t1 = time.time()
        print(f'TIME {t1 - t0}')