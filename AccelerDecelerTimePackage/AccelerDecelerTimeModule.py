from ApplicationModule import ApplicationModule
from CallBackOperators.TimeRegimeOperator import TimeRegimeOperator
from CallBackOperators.AccDecTimeOperator import AccDecTimeOperator


class AccelerDecelerTimeModule(ApplicationModule):

    def __init__(self):
        super().__init__()


    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                TimeRegimeOperator(),
                AccDecTimeOperator()
            ]