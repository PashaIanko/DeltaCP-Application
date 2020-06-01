from abc import ABC, abstractmethod

class CallBackOperator(ABC):

    @abstractmethod
    def ConnectCallBack(self, window):
        pass
