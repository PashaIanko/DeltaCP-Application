from abc import ABCMeta, abstractmethod
from SignalGenerationPackage.SignalData import SignalData
import statistics
from abc import abstractproperty



class Signal(metaclass=ABCMeta):

    # Model in MVC, abstract class
    # Aggregates the class SignalData - also part of the model, entity

    def __init__(self):
        self.SignalData = None  # abstract class
        self.Observers = []
        self.InitSignalData()

    @abstractmethod
    def InitSignalData(self):
        pass

    @abstractmethod
    def Func(self, x):
        pass


    @abstractmethod
    def UpdateSignalData(self):
        pass

    def UpdateDeltaTimes(self):
        N = len(SignalData.x)
        if N == 0:
            return  # No points at all
        elif N == 1:
            SignalData.dx.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00
        elif N > 1:
            SignalData.dx = [
                SignalData.x[dt_next_idx] - SignalData.x[dt_prev_idx]
                for dt_next_idx, dt_prev_idx
                in zip(range(1, N), range(0, N - 1))
            ]
            # TODO: В строке ниже - я не помню, с какой целью я вставлял лишнее dx в начало массива
            # SignalData.dx.insert(0, statistics.mean(SignalData.dx))  # Начальная точка отсчёта по времени, 0.00



    def RecalcData(self):
        self.UpdateSignalData()
        self.UpdateDeltaTimes()  # We calculate the array of dt values for optimization sakes, in the
                                # Signal Sending Module

    def AddObserver(self, Observer):
        self.Observers.append(Observer)

    def RemoveObserver(self, Observer):
        self.Observers.remove(Observer)

    def NotifyObservers(self):
        for observer in self.Observers:
            observer.UpdateModel()


