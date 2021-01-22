from ApplicationModule import ApplicationModule
from CallBackOperators.TimeRegimeOperator import TimeRegimeOperator

class AccelerDecelerTimeModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                TimeRegimeOperator(),
            ]