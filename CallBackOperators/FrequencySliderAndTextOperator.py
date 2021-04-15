from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from FrequencySettingPackage.FrequencySettingGUIParameters import FrequencySettingGUIParameters


class FrequencySliderAndTextOperator(CallBackOperator):
    def __init__(self, model=None, value_range=None):
        super().__init__(model, model, value_range)


    # overridden
    def init_slider(self):
        self.slider = self.window.FrequencySetSlider

    # overridden
    def init_line_edit(self):
        self.line_edit = self.window.OutputFrequencylineEdit

    def ConnectCallBack(self):
        self.SynchronizeSliderandText()

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
        value_to_set = self.window.FrequencySetSlider.value()
        value_to_set /= 10 ** FrequencySettingGUIParameters.FrequencyLineEditAccuracy  #  These calculations
                                                                # are for correct scaling on the slider
        text_to_set = str(value_to_set).replace('.', ',')
        self.window.OutputFrequencylineEdit.setText(str(text_to_set))

    # overridden
    def value_changed(self, val):
        pass





