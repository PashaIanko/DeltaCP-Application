from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.EdgeSignal.EdgeSignalData import EdgeSignalData
from SignalGenerationPackage.SignalData import SignalData


class EdgeSignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        pass

    def __init__(self):
        super().__init__()

    # overridden
    def InitSignalData(self):
        self.SignalData = EdgeSignalData()

    # overridden
    def Func(self, x):
        pass

    # overridden
    def UpdateSignalData(self):
        WholePeriod = self.SignalData.StartTime + self.SignalData.AccelerationTime + self.SignalData.PlateauTime + \
                      self.SignalData.DecelerationTime + self.SignalData.EndTime

        LowLevelFreq = self.SignalData.LowLevelFrequency
        HighLevelFreq = self.SignalData.HighLevelFrequency
        StartTime = self.SignalData.StartTime
        PlateauTime = self.SignalData.PlateauTime
        EndTime = self.SignalData.EndTime
        AccelerationTime = self.SignalData.AccelerationTime
        DecelerationTime = self.SignalData.DecelerationTime

        # Пересчёт необходимого времени разгона / замедления
        try:
            self.SignalData.NecessaryAccelerationTime = (self.SignalData.MaxFrequency - self.SignalData.MinFrequency) * \
                                                    (AccelerationTime / (LowLevelFreq - HighLevelFreq))

            self.SignalData.NecessaryDecelerationTime = (self.SignalData.MaxFrequency - self.SignalData.MinFrequency) * \
                                                    (DecelerationTime / (LowLevelFreq - HighLevelFreq))
        except ZeroDivisionError:
            pass  # В случае LowLevelFreq == HighLevelFreq может быть деление на 0. Здесь это допускается (т.к. пользователь
                  # редактирует сигнал. Далее, на этапе PIDSendingOperator (отправка сигнала) будет доп. проверка)

        if WholePeriod != 0:
            X_arr = [
                0,
                0 + StartTime,
                0 + StartTime + AccelerationTime,
                0 + StartTime + AccelerationTime + PlateauTime,
                0 + StartTime + AccelerationTime + PlateauTime + DecelerationTime,
                0 + StartTime + AccelerationTime + PlateauTime + DecelerationTime + EndTime
            ]

            Y_arr = [
                LowLevelFreq,
                LowLevelFreq,
                HighLevelFreq,
                HighLevelFreq,
                LowLevelFreq,
                LowLevelFreq
            ]

            SignalData.y = Y_arr
            SignalData.x = X_arr


    @property
    def AccelerationTime(self):
        return self.SignalData.AccelerationTime

    @AccelerationTime.setter
    def AccelerationTime(self, val):
        self.SignalData.AccelerationTime = val
        self.RecalcData()
        self.NotifyObservers()

    @property
    def EndTime(self):
        return self.SignalData.EndTime

    @EndTime.setter
    def EndTime(self, val):
        self.SignalData.EndTime = val
        self.RecalcData()
        self.NotifyObservers()

    @property
    def StartTime(self):
        return self.SignalData.StartTime

    @StartTime.setter
    def StartTime(self, val):
        self.SignalData.StartTime = val
        self.RecalcData()
        self.NotifyObservers()

    @property
    def DecelerationTime(self):
        return self.SignalData.DecelerationTime

    @DecelerationTime.setter
    def DecelerationTime(self, val):
        self.SignalData.DecelerationTime = val
        self.RecalcData()
        self.NotifyObservers()

    @property
    def HighLevelFrequency(self):
        return self.SignalData.HighLevelFrequency

    @HighLevelFrequency.setter
    def HighLevelFrequency(self, val):
        self.SignalData.HighLevelFrequency = val
        self.RecalcData()
        self.NotifyObservers()

    @property
    def LowLevelFrequency(self):
        return self.SignalData.LowLevelFrequency

    @LowLevelFrequency.setter
    def LowLevelFrequency(self, val):
        self.SignalData.LowLevelFrequency = val
        self.RecalcData()
        self.NotifyObservers()

    @property
    def PlateauTime(self):
        return self.SignalData.PlateauTime

    @PlateauTime.setter
    def PlateauTime(self, val):
        self.SignalData.PlateauTime = val
        self.RecalcData()
        self.NotifyObservers()

    @property
    def CriticalAcceleration(self):
        return self.SignalData.CriticalAcceleration

    @property
    def CriticalDeceleration(self):
        return self.SignalData.CriticalDeceleration