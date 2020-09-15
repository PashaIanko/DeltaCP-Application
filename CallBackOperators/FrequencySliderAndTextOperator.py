from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from FrequencySettingPackage.FrequencySettingGUIParameters import FrequencySettingGUIParameters


class FrequencySliderAndTextOperator(CallBackOperator):
    def __init__(self):
        self.window = None


    def ConnectCallBack(self, window):
        self.window = window

        FrequencyValueValidator = QDoubleValidator()
        FrequencyValueValidator.setRange(FrequencySettingGUIParameters.FrequencySliderMin,
                                         FrequencySettingGUIParameters.FrequencySliderMax,
                                         FrequencySettingGUIParameters.FrequencyLineEditAccuracy)
        window.OutputFrequencylineEdit.setValidator(FrequencyValueValidator)

        window.FrequencySetSlider.setMaximum(FrequencySettingGUIParameters.FrequencySliderMax)
        window.FrequencySetSlider.setMinimum(FrequencySettingGUIParameters.FrequencySliderMin)


        window.OutputFrequencylineEdit.textEdited.connect(self.UpdateFrequencySlider)
        window.FrequencySetSlider.valueChanged.connect(self.UpdateFrequencyLineEdit)


    def UpdateFrequencySlider(self):
        lineEditText = self.window.OutputFrequencylineEdit.text()

        if(len(lineEditText) == 0):
            lineEditText = '0'
        try:
            value = float(lineEditText) #* 10.0
            self.window.FrequencySetSlider.setValue(value * (10 ** FrequencySettingGUIParameters.FrequencyLineEditAccuracy))
        except:
            pass


    def UpdateFrequencyLineEdit(self):
        try:
            value_to_set = self.window.FrequencySetSlider.value()
            value_to_set /= 10 ** FrequencySettingGUIParameters.FrequencyLineEditAccuracy  #  These calculations
                                                                    # are for correct scaling on the slider
            text_to_set = str(value_to_set).replace('.', ',')
            self.window.OutputFrequencylineEdit.setText(str(text_to_set))

        except:
            print('caught!')




