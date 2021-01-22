from ApplicationModule import ApplicationModule
from CallBackOperators.SignalTypeOperator import SignalTypeOperator

class SignalGenerationModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                SignalTypeOperator()
            ]