from ApplicationModule import ApplicationModule
from CallBackOperators.NaiveSendingOperator import NaiveSendingOperator
from CallBackOperators.ForwardSendingOperator import ForwardSendingOperator


class SignalSendingModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                #NaiveSendingOperator()
                ForwardSendingOperator(DebugMode=True)
            ]
    # TODO: БАГ - когда запускаешь одиночный цикл отправки. Он доходит до конца. График закрываешь. Опять жмёшь Start - он пишет "Thread is executing, can't launch one"