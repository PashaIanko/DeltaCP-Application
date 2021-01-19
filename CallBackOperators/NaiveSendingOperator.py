from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator
from LoggersConfig import loggers


class NaiveSendingOperator(SignalSendingOperator):

    # Реализует "Наивную" отправку. На графика сигнала, по оси икс - моменты времени
    # по Y - какое значение сигнала отправить. Т.е. гарантируется, что в этот момент времени
    # Будет отправлено значение на графике. В новой стратегии (ForwardSendingOperator) реализовано
    # Так, чтобы в текущий момент времени мы не задали, а УЖЕ ИМЕЛИ данное значение
    # Как истинную частоту в этот момент времени.

    def __init__(self):
        super().__init__()

    # overridden
    def ExecuteSending(self, Time):
        DeltaTimes = SignalData.dx
        Dts_len = len(DeltaTimes)

        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 0
        self.TimeStamp = Time[self.PointsIterator]
        self.ValueToSend = SignalData.y[self.PointsIterator]


        print(f'INITIAL SEND: val={self.ValueToSend} at t={self.TimeStamp}')
        if self.Timer.if_started:  # Если уже дали старт таймеру на предудущем цикле
            self.Timer.reset(self.CycleGap)  # Время ожидания перед отправкой (так же перерыв между циклами)
        else:
            self.Timer.interval = self.CycleGap
            self.Timer.run()  # Подождали DeltaTimes[0] и отправили 0ую точку


        # После отправки нулевой точки - увеличиваем итератор
        self.PointsIterator += 1
        if Dts_len != 0:  # If the Time array has only one point, then we've already accomplished it in
                          # the method self.Timer.run()
            i = 0
            while i < Dts_len:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False

                    self.ValueToSend = SignalData.y[self.PointsIterator]
                    self.TimeStamp = Time[self.PointsIterator]
                    dt_to_wait = DeltaTimes[i] - self.CommandExecutionTime
                    print(f'SEND {self.ValueToSend} at the t={self.TimeStamp} after waiting for {dt_to_wait}')
                    self.Timer.reset(dt_to_wait)

                    i += 1
                    self.PointsIterator += 1

                if self.SendingStopped:
                    print('Stop push button --> finishing thread execution')
                    return

        while True: # Дожидаемся отправки последней команды (на краю сэмпла, чтобы на визуализации тоже это увидеть)
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                print(f'Finished CYCLE!')
                return


















