from ApplicationModule import ApplicationModule
from CallBackOperators.SignalTypeOperator import SignalTypeOperator

class SignalGenerationModule(ApplicationModule):

    callback_operators = \
        [
            SignalTypeOperator()
        ]

    def __init__(self):
        self.window = None

    def Run(self, window):
        self.window = window
        self.ConnectAllCallBacks()


    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.window)

