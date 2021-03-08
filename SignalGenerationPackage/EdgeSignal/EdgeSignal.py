from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.EdgeSignal.EdgeSignalData import EdgeSignalData
from SignalGenerationPackage.SignalData import SignalData
from SignalGenerationPackage.EdgeSignal.EdgeSignalTransformer import EdgeSignalTransformer
from SignalGenerationPackage.Point import Point


class EdgeSignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        pass

    def __init__(self):
        super().__init__()

    # overridden
    def InitSendingTransformer(self):
        self.SendingTransformer = EdgeSignalTransformer(self.SignalData)

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
        AccelerationTime = self.SignalData.AccelerationTime
        DecelerationTime = self.SignalData.DecelerationTime

        # Пересчёт необходимого времени разгона / замедления
        try:
            self.SignalData.NecessaryAccelerationTime = (self.SignalData.MaxFrequency - self.SignalData.MinFrequency) * \
                                                    (AccelerationTime / (HighLevelFreq - LowLevelFreq))

            self.SignalData.NecessaryDecelerationTime = (self.SignalData.MaxFrequency - self.SignalData.MinFrequency) * \
                                                    (DecelerationTime / (HighLevelFreq - LowLevelFreq))

            # Коэффициенты ускорения понадобятся для расчёта промежуточных точек
            # на разгоне / замедлении
            self.SignalData.AccelerationCoeff = (HighLevelFreq - LowLevelFreq) / AccelerationTime
            self.SignalData.DecelerationCoeff = (LowLevelFreq - HighLevelFreq) / DecelerationTime


        except ZeroDivisionError:
            pass  # В случае LowLevelFreq == HighLevelFreq может быть деление на 0. Здесь это допускается (т.к. пользователь
                  # редактирует сигнал. Далее, на этапе PIDSendingOperator (отправка сигнала) будет доп. проверка)

        if WholePeriod != 0:
            point_arr = self.get_point_array()
            SignalData.point_array = point_arr

    def get_point_array(self):
        res = []
        X_arr = self.get_X_arr()
        Y_arr = self.get_Y_arr()

        for x, y in zip(X_arr, Y_arr):
            res.append(Point(x=x, y=y, to_send=True))
        return res


    def get_Y_arr(self):
        # Изначальный массив
        LowFreq = self.SignalData.LowLevelFrequency  # TODO: Переписать через атрибуты
        HiFreq = self.SignalData.HighLevelFrequency
        PlateauTime = self.SignalData.PlateauTime
        StartTime = self.SignalData.StartTime
        EndTime = self.SignalData.EndTime
        res = [
            LowFreq,
            LowFreq,
            HiFreq,
            HiFreq,
            LowFreq,
            LowFreq
        ]
        if PlateauTime == 0:
            del res[3]
        if StartTime == 0:
            del res[0]
        if EndTime == 0:
            del res[-1]
        return res

    def get_X_arr(self):
        StartTime = self.SignalData.StartTime
        AccTime = self.SignalData.AccelerationTime
        PlateauTime = self.SignalData.PlateauTime
        DecTime = self.SignalData.DecelerationTime
        EndTime = self.SignalData.EndTime
        res = [
            0,
            0 + StartTime,
            0 + StartTime + AccTime,
            0 + StartTime + AccTime + PlateauTime,
            0 + StartTime + AccTime + PlateauTime + DecTime,
            0 + StartTime + AccTime + PlateauTime + DecTime + EndTime
        ]
        if PlateauTime == 0:
            # Убрать 3 точку (индекс с 0)
            del res[3]
        if StartTime == 0:
            del res[0]
        if EndTime == 0:
            del res[-1]
        return res

    # overridden
    def AddRequests_Y(self):
        points = SignalData.point_array_with_requests
        t_start = self.StartTime
        t_acc = self.AccelerationTime
        t_plateau = self.PlateauTime
        t_dec = self.DecelerationTime
        f_low = self.LowLevelFrequency
        f_hi = self.HighLevelFrequency
        acc = self.AccelerationCoeff
        dec = self.DecelerationCoeff

        lim0 = t_start
        lim1 = lim0 + t_acc
        lim2 = lim1 + t_plateau
        lim3 = lim2 + t_dec

        for p in points:
            if not p.to_send:
                x = p.x
                if x < lim0 or x >= lim3:
                    # Попадает на T_start, T_end
                    p.y = f_low
                elif lim1 <= x < lim2:
                    # Попадает на плато
                    p.y = f_hi
                elif lim0 <= x < lim1:
                    # Попадает на разгон
                    p.y = f_low + acc * (x - lim0)  # y = y_0 + k * (x - x0)
                elif lim2 <= x < lim3:
                    # Попадает на замедление
                    p.y = f_hi + dec * (x - lim2)

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

    @property
    def NecessaryAccelerationTime(self):
        return self.SignalData.NecessaryAccelerationTime

    @property
    def NecessaryDecelerationTime(self):
        return self.SignalData.NecessaryDecelerationTime

    @property
    def AccelerationCoeff(self):
        return self.SignalData.AccelerationCoeff

    @property
    def DecelerationCoeff(self):
        return self.SignalData.DecelerationCoeff