from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignalData import DynamicPointsDensitySignalData
from SignalGenerationPackage.SignalData import SignalData
import numpy as np
from PopUpNotifier.PopUpNotifier import PopUpNotifier


class DynamicPointsDensitySignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        pass

    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        self.SignalData = DynamicPointsDensitySignalData()

    def Func(self, x):
        pass


    def prepare_arr(self, time_from, time_to, subtract=False):
        x_arr = SignalData.x[
             (SignalData.x >= time_from) &
             (SignalData.x <= time_to)]

        if subtract:
            if len(x_arr) > 2:
                x_arr = [x_arr[0], x_arr[-1]]
        return x_arr

    def prepare_data_arr(self, time_from, time_to, points_density, endpoint=False, subtract=False):

        # Эта функция чисто для X_start, X_end, X_plateau. Для X_acceleration, X_deceleration
        # подход немного другой
        N = int(points_density * (time_to - time_from))
        if N == 1:
            # Нельзя, чтоб точка была одна, т.к. предполагается, что X_start, X_end, X_plateau
            # будут включать крайние точки (промежутки с включением, []), а X_acceleration, X_deceleration
            # не будут, т.е. состоят только из внутренних точек (промежуток типа ())
            N += 1
        x_arr = np.linspace(time_from, time_to, N, endpoint=endpoint)
        if subtract:
            if len(x_arr) > 2:
                x_arr = [x_arr[0], x_arr[-1]]
        return x_arr

    def prepare_acceleration_arr(self, time_from, time_to, tangent, endpoint=False): # TODO: Объединить prepare_acceleration_arr и prepare_deceleration_arr в обобщённую функцию
        points_density = self.SignalData.FittingConstant * self.SignalData.PointsDensity * (1 - (tangent / self.SignalData.CriticalAccelerationTangent))
        if points_density <= 0:
            return np.linspace(time_from, time_to, num=2, endpoint=endpoint)  # Значит, никаких внутренних точек не будет
                                                                                # num=2, потому что это 2 крайние точки (а внутренних нет)
        else:
            # Слишком часто точки подавать тоже нельзя, "сплошняком" - большие лаги
            if points_density >= self.SignalData.MaxPointsDensity:
                points_density = self.SignalData.MaxPointsDensity
            return self.prepare_data_arr(time_from, time_to, abs(points_density), endpoint, subtract=False)

    def prepare_deceleration_arr(self, time_from, time_to, tangent, endpoint=False):
        points_density = self.SignalData.FittingConstant * self.SignalData.PointsDensity * (1 - abs(tangent / self.SignalData.CriticalDecelerationTangent))
        if points_density <= 0:
            return np.linspace(time_from, time_to, num=2, endpoint=endpoint)
        else:
            # Слишком часто точки подавать тоже нельзя, "сплошняком" - большие лаги
            if points_density >= self.SignalData.MaxPointsDensity:
                points_density = self.SignalData.MaxPointsDensity
            return self.prepare_data_arr(time_from, time_to, points_density, endpoint, subtract=False)

    def UpdateSignalData(self):
        WholePeriod = self.SignalData.StartTime + self.SignalData.AccelerationTime + self.SignalData.PlateauTime + \
                      self.SignalData.DecelerationTime + self.SignalData.EndTime

        LowLevelFreq = self.SignalData.LowLevelFrequency
        HighLevelFreq = self.SignalData.HighLevelFrequency
        StartTime = self.SignalData.StartTime
        AccTime = self.SignalData.AccelerationTime
        PlateauTime = self.SignalData.PlateauTime
        DecTime = self.SignalData.DecelerationTime
        EndTime = self.SignalData.EndTime
        PointsDensity = self.SignalData.PointsDensity
        AccelerationTime = self.SignalData.AccelerationTime
        DecelerationTime = self.SignalData.DecelerationTime

        if WholePeriod != 0:
            StartX = self.prepare_data_arr(time_from=0,
                                           time_to=StartTime,
                                           points_density=PointsDensity,
                                           endpoint=True,
                                           subtract=True)


            if AccelerationTime != 0:
                AccelerationTangent = (HighLevelFreq - LowLevelFreq) / AccelerationTime
                AccelerationX = self.prepare_acceleration_arr(time_from=StartTime,
                                                              time_to=StartTime + AccTime,
                                                              tangent=AccelerationTangent,
                                                              endpoint=True)
                if len(StartX) != 0:
                    # Если на старте уже есть точки - крайнюю точку слева у ускорения убираем, чтоб два раза не учесть
                    AccelerationX = AccelerationX[1:]
            else: AccelerationX = []


            PlateauX = self.prepare_data_arr(time_from=StartTime + AccTime,
                                             time_to=StartTime + AccTime + PlateauTime,
                                             points_density=PointsDensity,
                                             endpoint=True,
                                             subtract=True)

            if DecelerationTime != 0:
                DecelerationTangent = (LowLevelFreq - HighLevelFreq) / DecelerationTime
                DecelerationX = self.prepare_deceleration_arr(time_from=StartTime + AccTime + PlateauTime,
                                                              time_to=StartTime + AccTime + PlateauTime + DecTime,
                                                              tangent=DecelerationTangent,
                                                              endpoint=True)
                if len(PlateauX):
                    # Значит, плато построено. И включает обе крайние точки, слева и справа (endpoint)
                    # Тогда надо убрать крайнюю правую точку на ускорении, и крайнюю левую точку у замедления,
                    # чтоб 2 раза не учесть
                    AccelerationX = AccelerationX[:-1]
                    DecelerationX = DecelerationX[1:]
            else: DecelerationX = []


            # Ещё был баг - если PlateauX = [], т.е. пустой, тогда края у AccelerationX и DecelerationX совпадают (
            # края на состыковке содержат одинаковые точки). У одного из массивов надо её убрать
            if len(PlateauX) == 0:
                # Допустим, убираем у DecelerationX
                DecelerationX = DecelerationX[1:]


            EndX = self.prepare_data_arr(time_from=StartTime + AccTime + PlateauTime + DecTime,
                                         time_to=StartTime + AccTime + PlateauTime + DecTime + EndTime,
                                         points_density=PointsDensity,
                                         endpoint=True,
                                         subtract=True)
            if len(EndX):
                # Значит, конечный отрезок построен, он включает и левую и правую крайние точки,
                # Так что у deceleration_x надо убрать крайнюю правую точку
                DecelerationX = DecelerationX[:-1]


            StartY = [LowLevelFreq for x in StartX]
            EndY = [LowLevelFreq for x in EndX]
            PlateauY = [HighLevelFreq for x in PlateauX]

            # Линейная зависимость виде y_0 + k * (x - x_0). Поэтому определим x_0 для
            # Участка с ускорением и замедлением
            AccelerationX0 = StartX[-1] if len(StartX) else 0
            if len(PlateauX):
                DecelerationX0 = PlateauX[-1]
            elif len(AccelerationX):
                DecelerationX0 = AccelerationX[-1]
            elif len(StartX):
                DecelerationX0 = StartX[-1]
            else:
                DecelerationX0 = 0

            AccelerationY = [LowLevelFreq + AccelerationTangent * (x - AccelerationX0) for x in AccelerationX]
            DecelerationY = [HighLevelFreq + DecelerationTangent * (x - DecelerationX0) for x in DecelerationX]

            # Подправляем баги на стыках линейных функций
            AccelerationY = [y if y <= HighLevelFreq else HighLevelFreq for y in AccelerationY]
            DecelerationY = [y if y >= LowLevelFreq else LowLevelFreq for y in DecelerationY]

            SignalData.y = StartY + AccelerationY + PlateauY + DecelerationY + EndY
            SignalData.x = np.concatenate((StartX, AccelerationX, PlateauX, DecelerationX, EndX))

            # проверим, что в SignalData.x после наших построений не попались повторяющиеся точки
            if not self.all_x_are_unique():
                PopUpNotifier.Error(f'X array in Signal contains non-unique values!\nThere will be an error during sending')

    @staticmethod
    def all_x_are_unique():
        return len(SignalData.x_with_requests) == len(set(SignalData.x_with_requests))

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
    def PointsDensity(self):
        return self.SignalData.PointsDensity

    @PointsDensity.setter
    def PointsDensity(self, val):
        self.SignalData.PointsDensity = val
        self.RecalcData()
        self.NotifyObservers()

