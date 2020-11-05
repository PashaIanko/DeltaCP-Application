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

