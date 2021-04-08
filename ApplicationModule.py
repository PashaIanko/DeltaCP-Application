from abc import ABC, abstractmethod


class ApplicationModule(ABC):

    def __init(self):
        self.UserInterface = None
        self.CallBackOperators = []

    def Run(self, UserInterface):
        self.UserInterface = UserInterface
        self.InitCallBackOperators(self.UserInterface)
        self.ConnectAllCallBacks()

    @abstractmethod
    def InitCallBackOperators(self, user_interface):
        pass

    def ConnectAllCallBacks(self):
        for conn in self.CallBackOperators:
            conn.ConnectCallBack()
