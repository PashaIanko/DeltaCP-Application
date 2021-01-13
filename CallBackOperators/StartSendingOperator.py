from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalTimer import SignalTimer
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator


class StartSendingOperator(SignalSendingOperator):

    def __init__(self):
        super().__init__()

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
                #print(f'inside while')
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


    def ThreadFunc(self):
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        # TODO: Check that TimeFrom <= TimeTo
        Time = SignalData.x.copy()
        self.SignalVisualizer.RefreshData(SignalData.x, SignalData.y)
        self.ExecuteSending(Time)


        while True:
            if self.SendingStopped == True:
                self.SendingStopped = False  # Reset the flag
                return
            elif self.EndlessSendingEnabled and self.CycleFinishedSuccessfully:
                # update Time array and restart the cycle
                self.CycleFinishedSuccessfully = False
                upd_val = SignalData.x[-1]
                for i in range(len(Time)):
                    Time[i] += upd_val + SignalData.dx[i]

                # restarting points Iterator, Visualisation and Sending Thread
                self.PointsIterator = 0
                self.SignalVisualizer.Restart(Time)
                self.ExecuteSending(Time)


    def Restart(self, Time):
        self.CycleFinishedSuccessfully = False
        upd_val = SignalData.x[-1]
        for i in range(len(Time)):
            Time[i] += upd_val + SignalData.dx[i]
        self.RestartSignalIterator()
        self.RestartVisualization(Time)
        self.ExecuteSending(Time)















