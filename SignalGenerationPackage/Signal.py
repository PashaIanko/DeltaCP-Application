from abc import ABCMeta, abstractmethod
from SignalGenerationPackage.SignalData import SignalData
import numpy as np


class Signal(metaclass=ABCMeta):

    # Model in MVC, abstract class
    # Aggregates the class SignalData - also part of the model, entity

    def __init__(self):
        self.SignalData = None  # abstract class
        self.Observers = []
        self.InitSignalData()
        self.RequestFreq = 2.0

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



    def RecalcData(self):
        self.UpdateSignalData()
        self.AddRequestData(self.RequestFreq)

        # Теперь обновить dt для x, y, x_with_requests, y_with_requests
        SignalData.dx = self.UpdateDeltaTimes(input=SignalData.x, output=SignalData.dx)  # We calculate the array of dt values for optimization sakes, in the
                                                                        # Signal Sending Module
        SignalData.dx_with_requests = self.UpdateDeltaTimes(input=SignalData.x_with_requests, output=SignalData.dx_with_requests)

    def AddRequestData(self, request_freq = 1.0):
        # Исходные данные - сам сигнал, SignalData.x, SignalData.y
        # Надо - зная частоту опроса, идём по всему массиву времени
        # dt = SignalData.x[i+1] - SignalData.x[i].
        # Если dt > 1 / request_freq --> Надо добавить "фиктивные точки" по времени
        # В этой точке, по прерыванию, будет только опрос, без отправки значения
        # на частотник

        dx = 1 / request_freq
        for prev_idx in range(0, len(SignalData.x) - 1):
            next_idx = prev_idx + 1
            x_prev = SignalData.x[prev_idx]
            x_next = SignalData.x[next_idx]
            dx_current = abs(x_next - x_prev)

            if dx_current > dx:
                # Значит, надо вставить точки для опроса
                x_from = x_prev
                x_to = x_next

                # Сколько точек вставить:
                N = int(dx_current * request_freq)

                # Массив x для вставки:
                x_new = np.linspace(x_from, x_to, N, endpoint=True)[1:-1]  # Нулевую и последнюю точку не берём,
                                                                            # Они были в исходном массиве
                # Массив y для вставки:
                y_new = [None] * len(x_new)  # Да, None это костыль. При отправке (SignalSendingOperator),
                                                # если значение 'y' == None, то не отправляем, а только запрашиваем
                                                # частоту
                # Вставляем x_new и y_new
                try:
                    SignalData.x_with_requests.append(x_prev)
                    SignalData.x_with_requests.extend(x_new)

                    SignalData.y_with_requests.append(None)
                    SignalData.y_with_requests.extend(y_new)

                    #SignalData.x = np.insert(SignalData.x, next_idx, x_new)
                    #SignalData.y = np.insert(SignalData.y, next_idx, y_new)
                except:
                    import sys

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


