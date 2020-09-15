from CallBackOperator import CallBackOperator


class SetAndStopFrequencyOperator(CallBackOperator):
    def __init__(self):
        self.window = None

    def ConnectCallBack(self, window):
        window.SetFrequencypushButton.clicked.connect(self.SetFrequency)
        window.StopFrequencypushButton.clicked.connect(self.StopSettingFrequency)
        self.window = window


    def SetFrequency(self):
        lineEditText = self.window.OutputFrequencylineEdit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0'

        lineEditText = lineEditText.replace(',', '.')
        print(f'setting {float(lineEditText)} frequency')


    def StopSettingFrequency(self):
        print(f'stop setting')
