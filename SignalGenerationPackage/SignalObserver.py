from abc import ABCMeta, abstractmethod

class SignalObserver(metaclass=ABCMeta):
    """
    Абстрактный суперкласс для всех наблюдателей.
    """
    def __init__(self, Controller, Model):
        self.Controller = Controller
        self.Model = Model
        self.Model.AddObserver(self)

    @abstractmethod
    def UpdateModel(self):
        pass