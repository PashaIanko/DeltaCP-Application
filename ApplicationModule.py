from abc import ABC, abstractmethod

class ApplicationModule(ABC):

    def __init(self):
        self.MainWindow = None # a class inherited from QMainWindow

    @abstractmethod
    def Run(self, window):
        pass

    @abstractmethod
    def ConnectAllCallBacks(self):
        pass
