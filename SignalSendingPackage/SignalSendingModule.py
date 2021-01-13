from ApplicationModule import ApplicationModule
from CallBackOperators.NaiveSendingOperator import NaiveSendingOperator
from CallBackOperators.ForwardSendingOperator import ForwardSendingOperator


class SignalSendingModule(ApplicationModule):

    callback_operators = \
        [
            NaiveSendingOperator()
            #ForwardSendingOperator(DebugMode=True)
        ]

    def __init__(self):
        self.window = None



    def Run(self, MainWindow):
        self.UserInterface = MainWindow.ui
        self.MainWindow = MainWindow
        self.ConnectAllCallBacks()


    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.UserInterface)  # TODO: В родителя!!! и убрать из дочерних классов этот код

