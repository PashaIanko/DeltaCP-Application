from ApplicationModule import ApplicationModule
from CallBackOperators.SignalTypeOperator import SignalTypeOperator

class SignalGenerationModule(ApplicationModule):

    def __init__(self):
        super().__init__()


    # overridden
    def InitCallBackOperators(self, user_interface):
        self.CallBackOperators = \
            [
                SignalTypeOperator(user_interface)
            ]