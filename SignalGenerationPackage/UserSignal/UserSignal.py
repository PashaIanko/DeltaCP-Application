from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.UserSignal.UserSignalData import UserSignalData
from SignalGenerationPackage.SignalData import SignalData
import numpy as np
import sys


class UserSignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        pass

    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        self.SignalData = UserSignalData()

    def Func(self, x):
        pass
        #return abs(self.SignalData.Amplitude * np.sin(self.SignalData.Omega * x + self.SignalData.Phase))

    def prepare_arr(self, time_from, time_to, subtract=False):
        x_arr = SignalData.x[
             (SignalData.x >= time_from) &
             (SignalData.x < time_to)]

        if subtract:
            if len(x_arr) > 2:
                x_arr = [x_arr[0], x_arr[-1]]
        return x_arr

    def UpdateSignalData(self):
        WholePeriod = self.SignalData.StartTime + self.SignalData.AccelerationTime + self.SignalData.PlateauTime + \
                      self.SignalData.DecelerationTime + self.SignalData.EndTime

        if WholePeriod != 0:
            WholePointsNumber = self.SignalData.PointsNumber
            SignalData.x = np.linspace(self.SignalData.X_from, WholePeriod, WholePointsNumber,
                                       endpoint=True)  # Пересчёт ГЛОБАЛЬНЫХ Переменных

            # Разобьём массив X на кусочки
            StartTime = self.SignalData.StartTime
            AccTime = self.SignalData.AccelerationTime
            PlateauTime = self.SignalData.PlateauTime
            DecTime = self.SignalData.DecelerationTime
            EndTime = self.SignalData.EndTime

            StartX = self.prepare_arr(time_from=0,
                                      time_to=StartTime,
                                      subtract=True)

            AccelerationX = self.prepare_arr(time_from=StartTime,
                                             time_to=StartTime + AccTime)

            PlateauX = self.prepare_arr(time_from=StartTime + AccTime,
                                        time_to=StartTime + AccTime + PlateauTime,
                                        subtract=True)

            DecelerationX = self.prepare_arr(time_from=StartTime + AccTime + PlateauTime,
                                             time_to=StartTime + AccTime + PlateauTime + DecTime)

            EndX = self.prepare_arr(time_from=StartTime + AccTime + PlateauTime + DecTime,
                                    time_to=StartTime + AccTime + PlateauTime + DecTime + EndTime,
                                    subtract=True)

            LowLevelFreq = self.SignalData.LowLevelFrequency
            HighLevelFreq = self.SignalData.HighLevelFrequency
            AccelerationCoeff = (HighLevelFreq - LowLevelFreq) / self.SignalData.AccelerationTime
            DecelerationCoeff = (LowLevelFreq - HighLevelFreq) / self.SignalData.DecelerationTime

            StartY = [LowLevelFreq for x in StartX]
            EndY = [LowLevelFreq for x in EndX]
            PlateauY = [HighLevelFreq for x in PlateauX]

            # Линейная зависимость виде y_0 + k * (x - x_0). Поэтому определим x_0 для
            # Участка с ускорением и замедлением
            if len(StartX):
                AccelerationX0 = StartX[-1]
            else:
                AccelerationX0 = 0

            if len(PlateauX):
                DecelerationX0 = PlateauX[-1]
            elif len(AccelerationX):
                DecelerationX0 = AccelerationX[-1]
            elif len(StartX):
                DecelerationX0 = StartX[-1]
            else:
                DecelerationX0 = 0

            AccelerationY = [LowLevelFreq + AccelerationCoeff * (x - AccelerationX0) for x in AccelerationX]
            DecelerationY = [HighLevelFreq + DecelerationCoeff * (x - DecelerationX0) for x in DecelerationX]

            # Подправляем баги на стыках линейных функций
            AccelerationY = [y if y <= HighLevelFreq else HighLevelFreq for y in AccelerationY]
            DecelerationY = [y if y >= LowLevelFreq else LowLevelFreq for y in DecelerationY]

            SignalData.y = StartY + AccelerationY + PlateauY + DecelerationY + EndY
            SignalData.x = np.concatenate((StartX, AccelerationX, PlateauX, DecelerationX, EndX))

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

    @property
    def x(self):
        return SignalData.x  # TODO: В родительский класс переместить это!!

    @property
    def y(self):
        return SignalData.y

