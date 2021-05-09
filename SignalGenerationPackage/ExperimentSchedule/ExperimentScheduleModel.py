from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleData import ExperimentScheduleData
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleTransformer import ExperimentScheduleTransformer
from SignalGenerationPackage.SignalData import SignalData
from SignalGenerationPackage.Point import Point


class ExperimentScheduleModel(Signal):

    # Model in MVC pattern

    def __init__(self):
        super().__init__()
        self.PlatoOffset = 0.01  # Это необходимо для
        # get_X_arr() функции. Для построения плато из заданных частот (
        # две точки на стыках плато будут лежать почти рядом, на расстоянии PlatoOffset
        # по оси X)

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
        X_arr = self.get_X_arr()  # TODO: Дублируемый код с EdgeSignal. Они оба наследуются модели, поэтому часть методов сделать абстрактными (например, get_X_arr, get_Y_arr)
        Y_arr = self.get_Y_arr()
        for x, y in zip(X_arr, Y_arr):
            res.append(Point(x=x, y=y, to_send=True))
        return res

    def get_X_arr(self):
        res = [0]  # начальная точка отсчёта
        for i in range(0, len(self.seconds)):
            res.append(sum(self.seconds[0:i + 1]) - self.PlatoOffset)
            res.append(sum(self.seconds[0:i+1]))
        return res

    def get_Y_arr(self):
        res = []
        for f in self.frequencies:
            res.extend([f, f])  # Частоты дублируются для создания "полочек" на графике, плато
        res.append(self.frequencies[-1])
        return res


    def AddRequests_X(self):  # TODO: сделать этот метод абстрактным

        request_every_N_sec = self.request_every_N_sec
        point_arr = SignalData.transformed_point_array

        for prev_idx in range(0, len(point_arr) - 1):
            next_idx = prev_idx + 1

            x_prev = point_arr[prev_idx].x
            y_prev = point_arr[prev_idx].y
            to_send_prev = point_arr[prev_idx].to_send

            x_next = point_arr[next_idx].x
            y_next = point_arr[next_idx].y
            to_send_next = point_arr[next_idx].to_send

            dx = x_next - x_prev

            if dx >= request_every_N_sec:
                N_requests = int(dx / request_every_N_sec)
                if N_requests == 0:
                    pass




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