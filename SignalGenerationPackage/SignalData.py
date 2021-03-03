from abc import abstractmethod, ABCMeta


class SignalData(metaclass=ABCMeta):

    # A part of Model in MVC pattern
    x = []
    y = []
    dx = []  # Array of dx values, for optimization sakes in the SignalSendingModule

    x_with_requests = []
    y_with_requests = []
    dx_with_requests = []

    x_to_send = []
    y_to_send = []

    def __init__(self):
        pass