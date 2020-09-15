from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
from FrequencySettingPackage.FrequencySettingGUIParameters import FrequencySettingGUIParameters


class FrequencySliderAndTextOperator(CallBackOperator):
    def __init__(self):
        self.window = None


    def ConnectCallBack(self, window):
        self.window = window


        #window.OutputFrequencylineEdit.setValidator(QDoubleValidator(
        #    FrequencySettingGUIParameters.FrequencySliderMin,
        #    FrequencySettingGUIParameters.FrequencySliderMax,
        #    2))
        # window.OutputFrequencylineEdit.setValidator(QDoubleValidator(0.0, 100.0, 2))

        window.OutputFrequencylineEdit.textEdited.connect(self.UpdateFrequencySlider)
        window.FrequencySetSlider.valueChanged.connect(self.UpdateFrequencyLineEdit)

    def UpdateFrequencySlider(self):
        lineEditText = self.window.OutputFrequencylineEdit.text()

        if(len(lineEditText) == 0):
            lineEditText = '0'
        try:
            value = float(lineEditText) * 10.0
            self.window.FrequencySetSlider.setValue(value)
        except:
            pass

    def UpdateFrequencyLineEdit(self):
        try:
            self.window.OutputFrequencylineEdit.setText(str(self.window.FrequencySetSlider.value() / 10))
        except:
            print('caught!')




