from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.UserSignal.UserSignalData import UserSignalData
from SignalGenerationPackage.SignalData import SignalData
import numpy as np
import statistics


class UserSignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        print(f'UserSignal in __repr__ method')


    def __init__(self):
        super().__init__()


    def InitSignalData(self):
        self.SignalData = UserSignalData()

    def Func(self, x):
        return abs(self.SignalData.Amplitude * np.sin(self.SignalData.Omega * x + self.SignalData.Phase))

    def UpdateSignalData(self):
        SignalData.x = np.linspace(self.SignalData.X_from, self.SignalData.X_to, self.SignalData.PointsNumber,
                                   endpoint=True)  # Пересчёт ГЛОБАЛЬНЫХ Переменных
        SignalData.y = [self.Func(x) for x in SignalData.x]  # TODO: X_From, X_To запихать в родителя


    @property
    def AccelerationTime(self):
        return self.SignalData.AccelerationTime


    @AccelerationTime.setter
    def AccelerationTime(self, val):
        self.SignalData.AccelerationTime = val
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
    def PointsNumber(self):
        return self.SignalData.PointsNumber

    @PointsNumber.setter
    def PointsNumber(self, val):
        self.SignalData.PointsNumber = val
        self.RecalcData()
        self.NotifyObservers()


    @property
    def VerticalOffset(self):
        return self.SignalData.VerticalOffset


    @VerticalOffset.setter
    def VerticalOffset(self, val):
        self.SignalData.VerticalOffset = val
        self.RecalcData()
        self.NotifyObservers()


    @property
    def X_to(self):
        return self.SignalData.X_to


    @X_to.setter
    def X_to(self, val):
        self.SignalData.X_to = val
        self.RecalcData()
        self.NotifyObservers()

