from abc import ABC, ABCMeta, abstractmethod
from PyQt5 import QtWidgets


class SignalController(QtWidgets.QMainWindow):

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

