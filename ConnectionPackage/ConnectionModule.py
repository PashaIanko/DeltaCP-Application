from ApplicationModule import ApplicationModule
from CallBackOperators.ComboBoxConnector import ComboBoxOperator
from CallBackOperators.ConnectionOperator import ConnectionOperator
from CallBackOperators.AutoConnectOperator import AutoConnectOperator


class ConnectionModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    # overridden
    def InitCallBackOperators(self, user_interface):
        self.CallBackOperators = \
            [
                ComboBoxOperator(user_interface),
                ConnectionOperator(user_interface),
                AutoConnectOperator(user_interface)
            ]