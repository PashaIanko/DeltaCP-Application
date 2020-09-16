from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient


class SetAndStopFrequencyOperator(CallBackOperator):
    def __init__(self):
        self.window = None
        self.client = DeltaCPClient()

    def ConnectCallBack(self, window):
        window.SetFrequencypushButton.clicked.connect(self.SetFrequency)
        window.StopFrequencypushButton.clicked.connect(self.StopSettingFrequency)
        self.window = window


    def SetFrequency(self):
        lineEditText = self.window.OutputFrequencylineEdit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0.0'

        lineEditText = lineEditText.replace(',', '.')
        self.client.SetFrequency(float(lineEditText))


    def StopSettingFrequency(self):
        self.client.SetFrequency(0.0)
