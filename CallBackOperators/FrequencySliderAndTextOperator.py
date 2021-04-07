from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from FrequencySettingPackage.FrequencySettingGUIParameters import FrequencySettingGUIParameters


class FrequencySliderAndTextOperator(CallBackOperator):
    def __init__(self, ValueRange=None):
        self.window = None
        self.slider = None
        self.line_edit = None
        self.changing_value = False
        self.value_range = ValueRange

    def ConnectCallBack(self, window):
        self.window = window
        self.slider = window.FrequencySetSlider
        self.line_edit = window.OutputFrequencylineEdit


        FrequencyValueValidator = QDoubleValidator()
        FrequencyValueValidator.setRange(FrequencySettingGUIParameters.FrequencySliderMin,
                                         FrequencySettingGUIParameters.FrequencySliderMax,
                                         FrequencySettingGUIParameters.FrequencyLineEditAccuracy)
        window.OutputFrequencylineEdit.setValidator(FrequencyValueValidator)

        self.slider.setMaximum(FrequencySettingGUIParameters.FrequencySliderMax)
        self.slider.setMinimum(FrequencySettingGUIParameters.FrequencySliderMin)


        #self.slider.valueChanged.connect(self.UpdateFrequencyLineEdit)
        #self.line_edit.textEdited.connect(self.UpdateFrequencySlider)
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.line_edit.textEdited.connect(self.text_changed)

    def text_changed(self):
        if self.changing_value:
            return
        self.changing_value = True

        val = self.get_line_edit_value()
        if val is not None:
            self.set_slider_value(val)
            self.value_changed(val)

        self.changing_value = False

    def set_slider_value(self, val):
        tmp = self.squeeze(val, self.value_range.min, self.value_range.max)
        self.slider.setValue(self.stretch(tmp, self.slider.minimum(), self.slider.maximum()))


    def get_line_edit_value(self):
        if not self.line_edit.hasAcceptableInput():
            return None
        return self.line_edit.locale().toDouble(self.line_edit.text())[0]

    def slider_value_changed(self):
        if self.changing_value:
            return
        self.changing_value = True

        value = self.get_slider_value()
        self.set_line_edit_value(value)
        self.value_changed(value)

        self.changing_value = False

    def set_line_edit_value(self, val):
        self.line_edit.setText(self.line_edit.locale().toString(float(val), 'f', self.value_range.decimals))


    def get_slider_value(self):
        tmp = self.squeeze(self.slider.value(), self.slider.minimum(), self.slider.maximum())
        return self.stretch(tmp, self.value_range.min, self.value_range.max)


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





