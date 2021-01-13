from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator


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
        N = len(DeltaTimes)

        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 0
        self.TimeStamp = Time[self.PointsIterator]
        self.ValueToSend = SignalData.y[self.PointsIterator]

        if self.Timer.if_started:  # Если уже дали старт таймеру на предудущем цикле
            self.Timer.reset(DeltaTimes[0] - self.CommandExecutionTime)
        else:
            self.Timer.interval = DeltaTimes[0] - self.CommandExecutionTime
            self.Timer.run()

        if N != 1:  # If the Time array has only one point, then we've already accomplished it in
                    # the method self.Timer.run()
            i = 0
            i_limit = N - 1
            while i < i_limit:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False
                    i += 1
                    self.PointsIterator += 1
                    self.ValueToSend = SignalData.y[self.PointsIterator]
                    self.TimeStamp = Time[self.PointsIterator]
                    self.Timer.reset(DeltaTimes[i] - self.CommandExecutionTime)

                if self.SendingStopped:
                    print('Stop push button --> finishing thread execution')
                    return
        while True: # Дожидаемся отправки последней команды (на краю сэмпла, чтобы на визуализации тоже это увидеть)
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                print(f'Finished CYCLE!')
                return


















