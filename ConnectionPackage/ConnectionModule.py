from ApplicationModule import ApplicationModule
from CallBackOperators.ComboBoxConnector import ComboBoxOperator
from CallBackOperators.ConnectionOperator import ConnectionOperator


class ConnectionModule(ApplicationModule):

    callback_operators = \
        [
            ComboBoxOperator(),
            ConnectionOperator()
        ]

    def __init__(self):
        self.window = None

    def Run(self, window):
        self.window = window
        self.ConnectAllCallBacks()


    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.window)

