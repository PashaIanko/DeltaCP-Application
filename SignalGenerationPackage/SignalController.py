from abc import ABC, ABCMeta, abstractmethod
from PyQt5 import QtWidgets

class DerivedMeta(type(QtWidgets.QMainWindow), ABCMeta):
    pass

class SignalController(DerivedMeta):

    '''
    In MVC pattern - this is the core that aggregates Model and View
    '''

    def __init__(self):
        super().__init__()
        self.callback_operators = []
        self.signal = None  # Model
        self.SignalObserver = None  # View

    @abstractmethod
    def InitSignalUI(self):
        pass

