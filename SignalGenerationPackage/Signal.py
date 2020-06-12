from abc import ABCMeta, abstractmethod
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

    def AddObserver(self, Observer):
        self.Observers.append(Observer)

    def RemoveObserver(self, Observer):
        self.Observers.remove(Observer)

    def NotifyObservers(self):
        for observer in self.Observers:
            observer.UpdateModel()


