from ApplicationModule import ApplicationModule
from CallBackOperators.ComboBoxConnector import ComboBoxOperator
from CallBackOperators.ConnectionOperator import ConnectionOperator
from CallBackOperators.AutoConnectOperator import AutoConnectOperator
from LoggersConfig import loggers


class ConnectionModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    # overridden
    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                ComboBoxOperator(),
                ConnectionOperator(),
                AutoConnectOperator()
            ]