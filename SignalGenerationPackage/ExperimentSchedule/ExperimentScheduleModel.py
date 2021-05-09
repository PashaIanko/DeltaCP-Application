from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleData import ExperimentScheduleData
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleTransformer import ExperimentScheduleTransformer
from SignalGenerationPackage.SignalData import SignalData
from SignalGenerationPackage.Point import Point


class ExperimentScheduleModel(Signal):

    # Model in MVC pattern

    def __init__(self):
        super().__init__()

    # overridden
    def InitSendingTransformer(self):
        self.SendingTransformer = ExperimentScheduleTransformer(self.SignalData)

    # overridden
    def InitSignalData(self):
        self.SignalData = ExperimentScheduleData()

    # overridden
    def Func(self, x):
        pass

    # overridden
    def UpdateSignalData(self):
        self.whole_length = sum(self.seconds)
        point_array = self.get_point_array()
        SignalData.point_array = point_array

    def get_point_array(self):
        res = []
        X_arr = self.get_X_arr()  # TODO: Дублируемый код с EdgeSignal. Они оба наследуются от
                                    # модели, поэтому часть методов сделать абстрактными (например, get_X_arr, get_Y_arr)
        Y_arr = self.get_Y_arr()

        for x, y in zip(X_arr, Y_arr):
            res.append(Point(x=x, y=y, to_send=True))

    def get_X_arr(self):
        res = [0]  # начальная точка отсчёта
        for i in range(0, len(self.seconds)):
            res.append(sum(self.seconds[0:i+1]))
        return res



    # overridden
    def AddRequests_Y(self):
        pass

    @property
    def whole_length(self):
        return self.SignalData.whole_length

    @whole_length.setter
    def whole_length(self, val):
        self.SignalData.whole_length = val

    @property
    def frequencies(self):
        return self.SignalData.frequencies

    @frequencies.setter
    def frequencies(self, freq_arr):
        self.SignalData.frequencies = freq_arr
        self.RecalcData()
        self.NotifyObservers()

    @property
    def seconds(self):
        return self.SignalData.seconds

    @seconds.setter
    def seconds(self, seconds_arr):
        self.SignalData.seconds = seconds_arr
        self.RecalcData()
        self.NotifyObservers()

    @property
    def request_every_N_sec(self):
        return self.SignalData.request_every_N_sec

    @request_every_N_sec.setter
    def request_every_N_sec(self, val):
        self.SignalData.request_every_N_sec = val
        self.RecalcData()
        self.NotifyObservers()