from abc import ABC, abstractmethod
from LoggersConfig import loggers

class ApplicationModule(ABC):

    def __init(self):
        self.MainWindow = None  # a class inherited from QMainWindow
        self.UserInterface = None
        self.CallBackOperators = []

    def Run(self, MainWindow):
        self.InitCallBackOperators()
        self.MainWindow = MainWindow
        self.UserInterface = MainWindow.ui
        self.ConnectAllCallBacks()

    @abstractmethod
    def InitCallBackOperators(self):
        pass

    def ConnectAllCallBacks(self):
        loggers['Debug'].debug(f'ApplicationModule: ConnectAllCallBacks: operators={self.CallBackOperators}')
        for conn in self.CallBackOperators:
            conn.ConnectCallBack(self.UserInterface)
