from abc import abstractmethod, ABCMeta

class SignalData(metaclass=ABCMeta):

    # A part of Model in MVC pattern

    def __init__(self):
        self.x = []
        self.y = []
        self.x_from = 0
        self.x_to = 0
        self.Observers = []

    def AddObserver(self, Observer):
        self.Observers.append(Observer)

    def RemoveObserver(self, Observer):
        self.Observers.remove(Observer)

    def NotifyObservers(self):
        for observer in self.Observers:
            observer.ModelChanged()