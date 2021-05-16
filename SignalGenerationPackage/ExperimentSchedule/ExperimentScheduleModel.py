from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleData import ExperimentScheduleData
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleTransformer import ExperimentScheduleTransformer
from SignalGenerationPackage.SignalData import SignalData
from SignalGenerationPackage.Point import Point
import numpy as np


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
    def Recalc_X_Y(self):
        for p in SignalData.point_array:
            SignalData.x.append(p.x)
            SignalData.y.append(p.y)

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
        len_x = len(point_arr)

        for prev_idx in range(0, len(point_arr) - 1):
            next_idx = prev_idx + 1

            x_prev = point_arr[prev_idx].x
            y_prev = point_arr[prev_idx].y
            to_send_prev = point_arr[prev_idx].to_send

            x_next = point_arr[next_idx].x
            y_next = point_arr[next_idx].y
            to_send_next = point_arr[next_idx].to_send

            dx_current = x_next - x_prev

            if dx_current <= request_every_N_sec and next_idx == len_x - 1:
                # Значит, нет необходимости вставлять точки для опроса - текущий dx_current и так достаточно мал
                # На последней итерации вставляем крайние точки
                self.extend_edge_points([x_prev, x_next], [y_prev, y_next], to_send_list=[to_send_prev, to_send_next])
            elif dx_current <= request_every_N_sec and next_idx < len_x - 1:
                # Итерация не последняя - только левые крайние точки добавляем
                self.extend_edge_points([x_prev], [y_prev], to_send_list=[to_send_prev])

            elif dx_current > request_every_N_sec:
                # Значит, надо вставить точки для опроса
                # Сколько точек вставить:
                N = int(dx_current / request_every_N_sec)

                if N == 0:
                    # Так совпало - тогда только крайние точки вставляем
                    if next_idx < len_x - 1:
                        # итерация не последняя
                        self.extend_edge_points([x_prev], [y_prev], to_send_list=[to_send_prev])
                    else:
                        # итерация последняя - добавляем края
                        self.extend_edge_points([x_prev, x_next], [y_prev, y_next],
                                                to_send_list=[to_send_prev, to_send_next])
                else:
                    # Тогда вставим несколько промежуточных точек:
                    # Массив x для вставки:
                    # N + 2 в linspace - т.к. N - только промежуточные, а тут linspace c учётом крайних
                    x_new = np.linspace(x_prev, x_next, N + 2, endpoint=True)

                    # Массив y для вставки:
                    # Да, None это костыль. При отправке (SignalSendingOperator),
                    # если значение 'y' == None, то не отправляем, а только запрашиваем
                    # частоту
                    y_new = [y_prev] + [y_prev] * (len(x_new) - 2) + [y_next]

                    # Ещё один костыль - лист из булевых флагов to_send - отправлять мы
                    # будем или опрашивать
                    to_send_list = [to_send_prev] + [False] * (len(x_new) - 2) + [to_send_next]

                    # Если не последняя итерация - то необходимо исключить последнюю точку
                    # из массивов X и Y
                    # А если последняя - то она включится
                    if next_idx != len_x - 1:
                        x_new = x_new[0:-1]
                        y_new = y_new[0:-1]
                        to_send_list = to_send_list[0:-1]
                    self.extend_edge_points(x_new, y_new, to_send_list)

    # overridden
    def AddRequests_Y(self):
        pass  # Не нужно добавлять промежуточных, это просто плато, на этапе Add_reauests_X() я уже добавил
                # значения Y


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