from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from LoggersConfig import loggers


class TimeRegimeOperator(CallBackOperator):
    def __init__(self):
        super().__init__()
        self.DeltaCPClient = DeltaCPClient()

    def ConnectCallBack(self, window):
        self.window = window
        window.AccDec1radioButton.toggled.connect(self.set_regime_1)
        window.AccDec2radioButton.toggled.connect(self.set_regime_2)
        window.AccDec3radioButton.toggled.connect(self.set_regime_3)
        window.AccDec4radioButton.toggled.connect(self.set_regime_4)

    def set_regime_1(self):
        if self.window.AccDec1radioButton.isChecked():
            loggers['Debug'].debug(f'Setting regime 1')
            self.DeltaCPClient.SetRegime1()

    def set_regime_2(self):
        if self.window.AccDec2radioButton.isChecked():
            loggers['Debug'].debug(f'Setting regime 2')
            self.DeltaCPClient.SetRegime2()

    def set_regime_3(self):
        if self.window.AccDec3radioButton.isChecked():
            loggers['Debug'].debug(f'Setting regime 3')
            self.DeltaCPClient.SetRegime3()

    def set_regime_4(self):
        if self.window.AccDec4radioButton.isChecked():
            loggers['Debug'].debug(f'Setting regime 4')
            self.DeltaCPClient.SetRegime4()



