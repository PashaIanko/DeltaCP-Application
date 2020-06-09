from abc import ABCMeta, abstractmethod
from abc import abstractproperty



class Signal(metaclass=ABCMeta):

    # Model in MVC, abstract class
    # Aggregates the class SignalData - also part of the model, entity

    def __init(self):
        self.SignalData = None  # abstract class
        self.InitSignalData()

    @abstractmethod
    def InitSignalData(self):
        pass  # self.SignalData = SinusSignalData()

    @abstractmethod
    def Plot(self):
        pass

    @abstractmethod
    def Func(self):
        pass


