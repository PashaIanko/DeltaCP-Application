from CallBackOperator import CallBackOperator


class SetAndStopFrequencyOperator(CallBackOperator):
    def __init__(self):
        self.window = None

    def ConnectCallBack(self, window):
        window.SetFrequencypushButton.clicked.connect(self.SetFrequency)
        window.StopFrequencypushButton.clicked.connect(self.StopSettingFrequency)
        self.window = window


    def SetFrequency(self):
        print(f'setting frequency = ')


    def StopSettingFrequency(self):
        print(f'stop setting')
