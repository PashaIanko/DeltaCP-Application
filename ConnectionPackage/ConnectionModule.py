from ApplicationModule import ApplicationModule
from CallBackOperators.ComboBoxConnector import ComboBoxOperator
from CallBackOperators.ConnectionOperator import ConnectionOperator
from CallBackOperators.AutoConnectOperator import AutoConnectOperator


class ConnectionModule(ApplicationModule):

    callback_operators = \
        [
            ComboBoxOperator(),
            ConnectionOperator(),
            AutoConnectOperator()
        ]

    def __init__(self):
        self.window = None

    def Run(self, MainWindow):
        self.UserInterface = MainWindow.ui
        self.ConnectAllCallBacks()


    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.UserInterface)

