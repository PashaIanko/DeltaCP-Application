from abc import ABC, abstractmethod
from PyQt5.QtGui import QDoubleValidator


class CallBackOperator(ABC):

    @abstractmethod
    def ConnectCallBack(self, window):
        pass

    @staticmethod
    def setup_callback_and_synchronize_slider(
            validator_min,
            validator_max,
            validator_accuracy,
            line_edit,
            slider_min,
            slider_max,
            slider,
            update_slider_func,
            update_line_edit_func
    ):
        validator = QDoubleValidator()
        validator.setRange(validator_min, validator_max, validator_accuracy)
        line_edit.setValidator(validator)

        slider.setMaximum(slider_max)
        slider.setMinimum(slider_min)

        line_edit.textEdited.connect(update_slider_func)
        slider.valueChanged.connect(update_line_edit_func)



    def update_slider(self, line_edit, slider, calc_constant):
        line_edit_text = line_edit.text()

        if len(line_edit_text) == 0:
            line_edit_text = '0'

        line_edit_text = line_edit_text.replace(',', '.')
        value = float(line_edit_text)
        slider.setValue(value * calc_constant)

    def update_line_edit(self, line_edit, slider, calc_constant, update_model_func):
        value_to_set = slider.value()
        value_to_set /= calc_constant
        text_to_set = str(value_to_set).replace('.', ',')

        line_edit.setText(str(text_to_set))
        update_model_func(value_to_set)


