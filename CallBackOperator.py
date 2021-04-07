from abc import ABC, abstractmethod
from PyQt5.QtGui import QDoubleValidator


class CallBackOperator(ABC):
    def __init__(self, window=None, model=None, value_range=None):
        self.window = window

        self.slider = None
        self.line_edit = None
        self.model = model
        self.value_range = value_range

        self.changing_value = False
        self.value_range = value_range

        self.init_slider()
        self.init_line_edit()

    @abstractmethod
    def init_slider(self):
        pass  # Это для CallBackOperator'ов, ответственных за синхронизацию слайдера и текстового поля.
                # Если ваш оператор с такими не работает, просто переопределите метод и напишите pass, вам он не нужен

    @abstractmethod
    def init_line_edit(self):
        pass  # Это для CallBackOperator'ов, ответственных за синхронизацию слайдера и текстового поля.
                # Если ваш оператор с такими не работает, просто переопределите метод и напишите pass, вам он не нужен

    @abstractmethod
    def value_changed(self, val):
        pass

    @abstractmethod
    def ConnectCallBack(self):
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

    @staticmethod
    def squeeze(val, min, max):
        return (val - min) / (max - min)

    @staticmethod
    def stretch(val, min, max):
        return min + val * (max - min)

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




