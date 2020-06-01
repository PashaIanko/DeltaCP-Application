from abc import ABC, abstractmethod

class ApplicationModule(ABC):

    @abstractmethod
    def Run(self, window):
        pass

    @abstractmethod
    def ConnectAllCallBacks(self):
        pass
