from CallBackOperator import CallBackOperator


class SignalTypeOperator(CallBackOperator):
    def __init__(self):
        self.window = None

    def ConnectCallBack(self, window):
        window.SignalTypecomboBox.currentIndexChanged.connect(self.SetSignalType)
        self.window = window

    def SetSignalType(self):
        print('in callback')
