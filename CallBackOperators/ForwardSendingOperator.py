from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator


class ForwardSendingOperator(SignalSendingOperator):

    # Реализует отправку "наперёд". На графика сигнала, по оси икс - моменты времени
    # по Y - какое значение сигнала отправить. В текущий момент времени T отправляется
    # не текущее значение сигнала, а то, что соответствует следующему моменту времени.
    # Таким образом, нет гарантий, но вероятность больше, что в каждый момент T
    # Будет достигнута истинная частота Y, указанная на графике для этого момента времени
    # (А не просто выставлена в этот момент времени)

    def __init__(self):
        super().__init__()

    # overridden
    def ExecuteSending(self, Time):
        DeltaTimes = SignalData.dx
        N = len(DeltaTimes)

        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 1
        self.TimeStamp = Time[self.PointsIterator - 1]
        self.ValueToSend = SignalData.y[self.PointsIterator]  # Сигнал опережает теперь
        preset_value = SignalData.y[0]

        if self.IsFirstCycle == True:
            # На первом прогоне надо предварительно выставить начальную частоту
            self.IsFirstCycle = False
            self.PresetFrequency(preset_value)

        if self.Timer.if_started == True:  # Если уже дали старт таймеру на предудущем цикле
            self.Timer.reset(DeltaTimes[0] - self.CommandExecutionTime)
        else:
            self.Timer.interval = DeltaTimes[0] - self.CommandExecutionTime
            self.Timer.run()

        if N != 1:  # If the Time array has only one point, then we've already accomplished it in
                    # the method self.Timer.run()

            i = 1
            self.PointsIterator += 1
            while i < N:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False

                    if i == N - 1:
                        print(f'INSIDE CODE')
                        # Это значит, мы достигли конца отправляемого сигнала.
                        # Поскольку отправляем наперёд - надо отправить начальную точку сигнала,
                        # При этом подождав detaT[-1] (Последний временной отрезок)
                        # Тогда, когда цикл отправки возобновится - начальная точка уже была отправлена в
                        # Этом коде. Поэтому в новом цикле начинаем отправку не с 0й, а с 1ой точки.
                        self.ValueToSend = SignalData.y[0]
                        self.TimeStamp = Time[self.PointsIterator - 1]
                        self.Timer.reset(DeltaTimes[-1] - self.CommandExecutionTime)

                    else:
                        self.ValueToSend = SignalData.y[self.PointsIterator]
                        self.TimeStamp = Time[self.PointsIterator - 1]
                        dt_to_wait = DeltaTimes[i] - self.CommandExecutionTime

                        print(f'SENDING {self.ValueToSend} after DT = {dt_to_wait}')
                        self.Timer.reset(dt_to_wait)

                    i += 1
                    self.PointsIterator += 1

                if self.SendingStopped:
                    return

        while True:  # Дожидаемся отправки последней команды (на краю сэмпла, чтобы на визуализации тоже это увидеть)
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                print(f'Finished CYCLE!')
                return