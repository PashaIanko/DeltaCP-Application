from ApplicationModule import ApplicationModule
from CallBackOperators.StartSendingOperator import StartSendingOperator


class SignalSendingModule(ApplicationModule):

    callback_operators = \
        [
            StartSendingOperator()
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

