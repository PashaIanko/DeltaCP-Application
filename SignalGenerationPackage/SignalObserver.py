from abc import ABCMeta, abstractmethod

class SignalObserver(metaclass=ABCMeta):
    """
    Абстрактный суперкласс для всех наблюдателей.
    """
    @abstractmethod
    def UpdateModel(self):
        pass