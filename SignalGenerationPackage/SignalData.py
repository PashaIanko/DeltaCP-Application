from abc import abstractmethod, ABCMeta

class SignalData(metaclass=ABCMeta):

    # A part of Model in MVC pattern

    def __init__(self):
        self.x = []
        self.y = []
        self.x_from = 0
        self.x_to = 0
