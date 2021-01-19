from ApplicationModule import ApplicationModule
from CallBackOperators.TimeRegimeOperator import TimeRegimeOperator

class AccelerDecelerTimeModule(ApplicationModule):

    callback_operators = \
        [
            TimeRegimeOperator(),
        ]

    def __init__(self):
        super().__init__()

    def Run(self, MainWindow):
        self.MainWindow = MainWindow
        self.UserInterface = MainWindow.ui
        self.ConnectAllCallBacks()  # TODO: Перенести этот код в родителя


    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.UserInterface)  # TODO: код в родителя