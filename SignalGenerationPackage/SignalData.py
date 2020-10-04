from abc import abstractmethod, ABCMeta


class SignalData(metaclass=ABCMeta):

    # A part of Model in MVC pattern
    x = []
    y = []
    dx = []  # Array of dx values, for optimization sakes in the SignalSendingModule

    def __init__(self):
        pass



