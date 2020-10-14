from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.UserSignal.UserSignalData import UserSignalData
from SignalGenerationPackage.SignalData import SignalData
import numpy as np
import sys


class UserSignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        print(f'UserSignal in __repr__ method')

    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        self.SignalData = UserSignalData()

    def Func(self, x):
        pass
        #return abs(self.SignalData.Amplitude * np.sin(self.SignalData.Omega * x + self.SignalData.Phase))

    def UpdateSignalData(self):
        WholePeriod = self.SignalData.StartTime + self.SignalData.AccelerationTime + self.SignalData.PlateauTime + \
                      self.SignalData.DecelerationTime + self.SignalData.EndTime
        print(f'In Method UpdadteSignalData')
        if WholePeriod != 0:
            WholePointsNumber = self.SignalData.PointsNumber

            StartPercent = self.SignalData.StartTime / WholePeriod
            AccelerationPercent = self.SignalData.AccelerationTime / WholePeriod
            PlateauPercent = self.SignalData.PlateauTime / WholePeriod
            DecelerationPercent = self.SignalData.DecelerationTime / WholePeriod
            # EndPercent = self.SignalData.EndTime / WholePeriod

            # Три порции точек - На acceleration, plateau и deceleration
            StartPoints = int(WholePointsNumber * StartPercent)
            AccelerationPoints = int(WholePointsNumber * AccelerationPercent)
            PlateauPoints = int(WholePointsNumber * PlateauPercent)
            DecelerationPoints = int(WholePointsNumber * DecelerationPercent)
            # EndPoints = WholePointsNumber - (StartPoints + AccelerationPoints + PlateauPoints + DecelerationPoints)

            try:
                SignalData.x = np.linspace(self.SignalData.X_from, WholePeriod, WholePointsNumber,
                                       endpoint=True)  # Пересчёт ГЛОБАЛЬНЫХ Переменных
            except:
                print(f' After Sign.x')
                print(sys.exc_info())

            # Разобьём массив X на кусочки
            try:
                StartX = SignalData.x[0: StartPoints]
                AccelerationX = SignalData.x[StartPoints: StartPoints + AccelerationPoints]
                PlateauX = SignalData.x[StartPoints + AccelerationPoints: StartPoints + AccelerationPoints + PlateauPoints]
                DecelerationX = SignalData.x[StartPoints + AccelerationPoints + PlateauPoints:
                                             DecelerationPoints + StartPoints + AccelerationPoints + PlateauPoints]
                EndX = SignalData.x[DecelerationPoints + StartPoints + AccelerationPoints + PlateauPoints:
                                    WholePointsNumber]
            except:
                print('Caught here!!')

            try:
                LowLevelFreq = self.SignalData.LowLevelFrequency
                HighLevelFreq = self.SignalData.HighLevelFrequency
                AccelerationCoeff = (HighLevelFreq - LowLevelFreq) / self.SignalData.AccelerationTime
                DecelerationCoeff = -(HighLevelFreq - LowLevelFreq) / self.SignalData.DecelerationTime

                StartY = [LowLevelFreq for x in StartX]
                AccelerationY = [LowLevelFreq + AccelerationCoeff * x for x in AccelerationX]
                PlateauY = [HighLevelFreq for x in PlateauX]
                DecelerationY = [HighLevelFreq + DecelerationCoeff * x for x in DecelerationX]
                EndY = [LowLevelFreq for x in EndX]
            except:
                print('CAUGHT HERE')

            SignalData.y = StartY + AccelerationY + PlateauY + DecelerationY + EndY
            #[self.Func(x) for x in SignalData.x]  # TODO: X_From, X_To запихать в родителя

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

    # @property
    # def X_to(self):
    #     return self.SignalData.X_to
    #
    # @X_to.setter
    # def X_to(self, val):
    #     self.SignalData.X_to = val
    #     self.RecalcData()
    #     self.NotifyObservers()

    @property
    def x(self):
        return SignalData.x  # TODO: В родительский класс переместить это!!

    @property
    def y(self):
        return SignalData.y  # self.SignalData.y # Возвращаются глобальные перем (class attributes) - x и y

