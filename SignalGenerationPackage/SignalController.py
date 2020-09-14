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

        # defining customized user interface
        self.UserInterface = None
        self.MainWindow = QtWidgets.QMainWindow()  # new window with graphical interface
        self.InitSignalUI()  # overridden method - each class implements own User Interface

        self.UserInterface.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.InitModel()  # overriden
        self.InitView()  # overriden
        self.InitCallBackOperators()  # overriden
        self.ConnectCallBacks()  # overriden

    @abstractmethod
    def InitSignalUI(self):
        pass

    @abstractmethod
    def InitModel(self):
        # creating MVC model
        pass

    @abstractmethod
    def InitView(self):
        # creating MVC view
        pass

    @abstractmethod
    def InitCallBackOperators(self):
        pass

    @abstractmethod
    def ConnectCallBacks(self):
        pass

