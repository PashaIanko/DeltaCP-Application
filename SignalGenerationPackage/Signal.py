from abc import ABCMeta, abstractmethod
from SignalGenerationPackage.SignalData import SignalData
import numpy as np
from LoggersConfig import loggers


class Signal(metaclass=ABCMeta):

    # Model in MVC, abstract class
    # Aggregates the class SignalData - also part of the model, entity

    def __init__(self):
        self.SignalData = None  # abstract class
        self.Observers = []
        self.InitSignalData()
        self.RequestFreq = 1.0

    @abstractmethod
    def InitSignalData(self):
        pass

    @abstractmethod
    def Func(self, x):
        pass


    @abstractmethod
    def UpdateSignalData(self):
        pass

    def UpdateDeltaTimes(self, input, output):
        N = len(input)
        if N == 0:
            return  # No points at all
        elif N == 1:
            output.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00
        elif N > 1:
            output = [
                input[dt_next_idx] - input[dt_prev_idx]
                for dt_next_idx, dt_prev_idx
                in zip(range(1, N), range(0, N - 1))
            ]
        return output
            # TODO: В строке ниже - я не помню, с какой целью я вставлял лишнее dx в начало массива
            # SignalData.dx.insert(0, statistics.mean(SignalData.dx))  # Начальная точка отсчёта по времени, 0.00


    def ClearRequestData(self):
        SignalData.x_with_requests.clear()
        SignalData.y_with_requests.clear()

    def RecalcData(self):
        self.UpdateSignalData()
        self.ClearRequestData()
        self.AddRequestData(self.RequestFreq)

        # Теперь обновить dt для x, y, x_with_requests, y_with_requests
        SignalData.dx = self.UpdateDeltaTimes(input=SignalData.x, output=SignalData.dx)  # We calculate the array of dt values for optimization sakes, in the
                                                                        # Signal Sending Module
        SignalData.dx_with_requests = self.UpdateDeltaTimes(input=SignalData.x_with_requests, output=SignalData.dx_with_requests)

    @staticmethod
    def extend_edge_points(list_x, list_y):
        SignalData.x_with_requests.extend(list_x)
        SignalData.y_with_requests.extend(list_y)

    def AddRequestData(self, request_freq = 1.0):
        # Исходные данные - сам сигнал, SignalData.x, SignalData.y
        # Надо - зная частоту опроса, идём по всему массиву времени
        # dt = SignalData.x[i+1] - SignalData.x[i].
        # Если dt > 1 / request_freq --> Надо добавить "фиктивные точки" по времени
        # В этой точке, по прерыванию, будет только опрос, без отправки значения
        # на частотник

        dx = 1 / request_freq
        len_x = len(SignalData.x)
        for prev_idx in range(0, len_x - 1):
            next_idx = prev_idx + 1
            x_prev = SignalData.x[prev_idx]
            x_next = SignalData.x[next_idx]
            y_prev = SignalData.y[prev_idx]
            y_next = SignalData.y[next_idx]
            dx_current = abs(x_next - x_prev)

            if dx_current <= dx and next_idx == len_x - 1:
                # Значит, нет необходимости вставлять точки для опроса - текущий dx_current и так достаточно мал
                #self.extend_edge_points([x_prev, x_next], [y_prev, y_next])
                # На последней итерации вставляем крайние точки
                self.extend_edge_points([x_prev, x_next], [y_prev, y_next])
            elif dx_current <= dx and next_idx < len_x - 1:
                # Итерация не последняя - только левые крайние точки добавляем
                self.extend_edge_points([x_prev], [y_prev])
            elif dx_current > dx:
                # Значит, надо вставить точки для опроса
                # Сколько точек вставить:
                N = int(dx_current * request_freq)

                if N == 0:
                    # Так совпало - тогда только крайние точки вставляем
                    if next_idx < len_x - 1:
                        # итерация не последняя
                        self.extend_edge_points([x_prev], [y_prev])
                    else:
                        # итерация последняя - добавляем края
                        self.extend_edge_points([x_prev, x_next], [y_prev, y_next])
                else:
                    # Тогда вставим несколько промежуточных точек:
                    # Массив x для вставки:
                    # N + 2 в linspace - т.к. N - только промежуточные, а тут linspace c учётом крайних
                    x_new = np.linspace(x_prev, x_next, N + 2, endpoint=True)

                    # Если не последняя итерация - то необходимо исключить последнюю точку
                    # А если последняя - то она включится
                    if next_idx != len_x - 1:
                        x_new = x_new[0:-1]

                    # Массив y для вставки:
                    # Да, None это костыль. При отправке (SignalSendingOperator),
                    # если значение 'y' == None, то не отправляем, а только запрашиваем
                    # частоту TODO: Исправить этот костыль
                    y_new = [y_prev] + [y_next] + [None] * (len(x_new) - 2) # + [y_next]

                    # Ещё костыль, чтобы не было дублирования точек - если не первая итерация -
                    # заменить начальную точку на None
                    if prev_idx > 0:
                        y_new[0] = None

                    # Вставляем x_new и y_new
                    try:
                        SignalData.x_with_requests.extend(x_new)
                        SignalData.y_with_requests.extend(y_new)
                    except:
                        import sys

                        loggers['Debug'].debug(f'Signal: AddRequestData: exception: {sys.exc_info()}')
        self.test_adding_requests()

    def test_adding_requests(self):
        l_y = [i in SignalData.y_with_requests for i in SignalData.y]
        l_x = [i in SignalData.x_with_requests for i in SignalData.x]
        loggers['Debug'].debug(f'Added Requests correctly?: for y: {not (False in l_y)}, for x: {not (False in l_x)}')

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