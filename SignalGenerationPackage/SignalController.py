from abc import ABCMeta, abstractmethod
from PyQt5 import QtWidgets

class SignalController(metaclass=ABCMeta):

    '''
    In MVC pattern - this is the core that aggregates Model and View
    '''

    def __init__(self):
        self.CallbackOperators = []
        self.Signal = None  # Model
        self.SignalObserver = None  # View
        self.MainWindow = QtWidgets.QMainWindow()  # new window with graphical interface
        self.InitSignalUI()

    @abstractmethod
    def InitSignalUI(self):
        pass

    @abstractmethod
    def ConnectCallBacks(self):
        pass

