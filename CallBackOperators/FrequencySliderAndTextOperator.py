from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
from FrequencySettingPackage.FrequencySettingGUIParameters import FrequencySettingGUIParameters


class FrequencySliderAndTextOperator(CallBackOperator):
    def __init__(self):
        self.window = None


    def ConnectCallBack(self, window):
        self.window = window


        window.OutputFrequencylineEdit.setValidator(QDoubleValidator(
            FrequencySettingGUIParameters.FrequencySliderMin,
            FrequencySettingGUIParameters.FrequencySliderMax,
            2))

        # window.OutputFrequencylineEdit.textChanged.connect(self.SetSlider)


