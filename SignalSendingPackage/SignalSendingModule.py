from ApplicationModule import ApplicationModule
from CallBackOperators.NaiveSendingOperator import NaiveSendingOperator
from CallBackOperators.ForwardSendingOperator import ForwardSendingOperator


class SignalSendingModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                # NaiveSendingOperator()
                ForwardSendingOperator(DebugMode=True)
            ]