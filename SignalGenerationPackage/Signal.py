from abc import ABCMeta, abstractmethod
from SignalGenerationPackage.SignalData import SignalData
import numpy as np
from LoggersConfig import loggers
from SignalGenerationPackage.Point import Point


class Signal(metaclass=ABCMeta):

    # Model in MVC, abstract class
    # Aggregates the class SignalData - also part of the model, entity

    def __init__(self):
        self.SignalData = None  # abstract class
        self.SendingTransformer = None
        self.Observers = []
        self.InitSignalData()
        self.InitSendingTransformer()
        self.RequestFreq = 1.0

    @abstractmethod
    def InitSignalData(self):
        pass

    @abstractmethod
    def InitSendingTransformer(self):
        pass

    @abstractmethod
    def Func(self, x):
        pass


    @abstractmethod
    def UpdateSignalData(self):
        pass

    def UpdateDeltaTimes(self):
        input = SignalData.point_array_with_requests
        output = []

        N = len(input)

        if N == 1:
            output.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00
        elif N > 1:
            output = [
                input[dt_next_idx].x - input[dt_prev_idx].x
                for dt_next_idx, dt_prev_idx
                in zip(range(1, N), range(0, N - 1))
            ]
        return output

    def RecalcData(self):
        self.ClearSignalData()
        self.UpdateSignalData()
        self.TransformSignal()  # Преобразовать для отправки # TODO: Может Transform и Request сделать по колбеку на StartSending?
        self.AddRequests_X()
        self.AddRequests_Y()
        SignalData.dx = self.UpdateDeltaTimes()
        self.Recalc_X_Y()

    @abstractmethod
    def Recalc_X_Y(self):
        pass

    def ClearSignalData(self):
        SignalData.x.clear()
        SignalData.y.clear()
        SignalData.dx.clear()
        SignalData.transformed_point_array.clear()
        SignalData.point_array.clear()
        SignalData.point_array_with_requests.clear()

    def TransformSignal(self):
        self.SendingTransformer.TransformSignal()

    @staticmethod
    def extend_edge_points(list_x, list_y, to_send_list):
        pts_arr = []
        for x, y, to_send in zip(list_x, list_y, to_send_list):
            point = Point(x=x, y=y, to_send=to_send)
            pts_arr.append(point)
        SignalData.point_array_with_requests.extend(pts_arr)

    @abstractmethod
    def AddRequests_Y(self):
        # Уже добавили моменты времени для опроса.
        # Теперь надо пересчитать ожидаемую частоту в момент опроса.
        pass

    def AddRequests_X(self):

        # Исходные данные - сам сигнал, SignalData.x, SignalData.y
        # Надо - зная частоту опроса, идём по всему массиву времени
        # dt = SignalData.x[i+1] - SignalData.x[i].
        # Если dt > 1 / request_freq --> Надо добавить "фиктивные точки" по времени
        # В этой точке, по прерыванию, будет только опрос, без отправки значения
        # на частотник

        request_freq = self.RequestFreq
        point_arr = SignalData.transformed_point_array

        dx = 1 / request_freq
        len_x = len(point_arr)

        for prev_idx in range(0, len_x - 1):
            next_idx = prev_idx + 1
            x_prev = point_arr[prev_idx].x
            x_next = point_arr[next_idx].x
            y_prev = point_arr[prev_idx].y
            y_next = point_arr[next_idx].y
            to_send_prev = point_arr[prev_idx].to_send
            to_send_next = point_arr[next_idx].to_send
            dx_current = abs(x_next - x_prev)

            if dx_current <= dx and next_idx == len_x - 1:
                # Значит, нет необходимости вставлять точки для опроса - текущий dx_current и так достаточно мал
                # На последней итерации вставляем крайние точки
                self.extend_edge_points([x_prev, x_next], [y_prev, y_next], to_send_list=[to_send_prev, to_send_next])
            elif dx_current <= dx and next_idx < len_x - 1:
                # Итерация не последняя - только левые крайние точки добавляем
                self.extend_edge_points([x_prev], [y_prev], to_send_list=[to_send_prev])
            elif dx_current > dx:
                # Значит, надо вставить точки для опроса
                # Сколько точек вставить:
                N = int(dx_current * request_freq)

                if N == 0:
                    # Так совпало - тогда только крайние точки вставляем
                    if next_idx < len_x - 1:
                        # итерация не последняя
                        self.extend_edge_points([x_prev], [y_prev], to_send_list=[to_send_prev])
                    else:
                        # итерация последняя - добавляем края
                        self.extend_edge_points([x_prev, x_next], [y_prev, y_next], to_send_list=[to_send_prev, to_send_next])
                else:
                    # Тогда вставим несколько промежуточных точек:
                    # Массив x для вставки:
                    # N + 2 в linspace - т.к. N - только промежуточные, а тут linspace c учётом крайних
                    x_new = np.linspace(x_prev, x_next, N + 2, endpoint=True)

                    # Массив y для вставки:
                    # Да, None это костыль. При отправке (SignalSendingOperator),
                    # если значение 'y' == None, то не отправляем, а только запрашиваем
                    # частоту
                    y_new = [y_prev] + [None] * (len(x_new) - 2) + [y_next]

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

    def AddObserver(self, Observer):
        self.Observers.append(Observer)

    def RemoveObserver(self, Observer):
        self.Observers.remove(Observer)

    def NotifyObservers(self):
        for observer in self.Observers:
            observer.UpdateModel()

    @property
    def x(self):
        return SignalData.x

    @property
    def y(self):
        return SignalData.y

    @property
    def request_freq(self):
        return self.RequestFreq

    @request_freq.setter
    def request_freq(self, val):
        self.RequestFreq = val
        self.RecalcData()
        self.NotifyObservers()