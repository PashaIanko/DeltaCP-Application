from abc import ABC, abstractmethod


class ApplicationModule(ABC):

    def __init(self):
        self.UserInterface = None
        self.CallBackOperators = []

    def Run(self, UserInterface):
        self.InitCallBackOperators()
        self.UserInterface = UserInterface
        self.ConnectAllCallBacks()

    @abstractmethod
    def InitCallBackOperators(self):
        pass

    def ConnectAllCallBacks(self):
        for conn in self.CallBackOperators:
            conn.ConnectCallBack(self.UserInterface)
