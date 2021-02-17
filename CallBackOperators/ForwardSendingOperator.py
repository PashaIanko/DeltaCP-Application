from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator
from LoggersConfig import loggers
from time import sleep

class ForwardSendingOperator(SignalSendingOperator):

    # Реализует отправку "наперёд". На графика сигнала, по оси икс - моменты времени
    # по Y - какое значение сигнала отправить. В текущий момент времени T отправляется
    # не текущее значение сигнала, а то, что соответствует следующему моменту времени.
    # Таким образом, нет гарантий, но вероятность больше, что в каждый момент T
    # Будет достигнута истинная частота Y, указанная на графике для этого момента времени
    # (А не просто выставлена в этот момент времени)

    def __init__(self, signal_main_window, DebugMode):
        super().__init__(signal_main_window, DebugMode)
        self.IsFirstCycle = True
        # На первом цикле исполнение - самую первую частоту задаём и ожидаем, пока не
        # достигнем её. Например, если первое значение = 30 Гц. Зададим и подождём, пока частотник достигнет
        # её. Только после этого продолжаем динамическую отправку

    # overridden
    def ExecuteSending(self, Time):
        DeltaTimes = SignalData.dx_with_requests
        Dts_len = len(DeltaTimes)

        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 1
        self.TimeStamp = Time[self.PointsIterator - 1]  # В какой момент времени на графике мы выставим ValueToSend
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
        if Dts_len != 1:  # If the Time array has only one point, then we've already accomplished it in
                          # the method self.Timer.run()

            i = 0
            self.PointsIterator += 1
            while i < Dts_len:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False

                    if i == Dts_len - 1:
                        # Это значит, мы достигли конца отправляемого сигнала.
                        # Поскольку отправляем наперёд - надо отправить начальную точку сигнала,
                        # При этом подождав detaT[-1] (Последний временной отрезок)
                        # Тогда, когда цикл отправки возобновится - начальная точка уже была отправлена в
                        # Этом коде. Поэтому в новом цикле начинаем отправку не с 0й, а с 1ой точки.
                        self.ValueToSend = SignalData.y_with_requests[0]
                        self.TimeStamp = Time[self.PointsIterator - 1]
                        loggers['SignalSending'].info(f'After dt={dt_to_wait} sec, I will send {self.ValueToSend} Hz')
                        self.Timer.reset(DeltaTimes[-1] - self.CommandExecutionTime)

                    else:
                        self.ValueToSend = SignalData.y_with_requests[self.PointsIterator]
                        self.TimeStamp = Time[self.PointsIterator - 1]
                        dt_to_wait = DeltaTimes[i] - self.CommandExecutionTime

                        loggers['SignalSending'].info(f'After dt={dt_to_wait} sec, I will send {self.ValueToSend} Hz')
                        self.Timer.reset(dt_to_wait)

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


    def PresetFrequency(self, value):
        # Перед запуском, если частота ненулевая - убедиться, предварительно задать требуемую начальную частоту
        value_to_send = int(value * 100)  # Привести к инту, иначе pymodbus выдаёт ошибку
        self.DeltaCPClient.SetFrequency(value_to_send)
        accuracy = 0.05

        if self.DebugMode:
            return
        else:
            while True:
                # мониторим, достигли ли требуемой начальной частоты
                sleep(1)
                current_freq = self.DeltaCPClient.RequestCurrentFrequency()
                loggers['Debug'].debug(f'ForwardSendingOperator: PresetFrequency: Current freq = {current_freq}, val to send = {value}')
                if abs(current_freq - value) <= accuracy:
                    return


