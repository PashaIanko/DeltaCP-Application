from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator


class FlowrateRecalcCallBackOperator(CallBackOperator):

    def __init__(self, window, model, value_range):
        super().__init__(window, model, value_range)
        self.proportion_line_edit = self.window.ProportionalityCoefficientlineEdit
        self.offset_line_edit = self.window.OffsetCoefficientlineEdit
        self.radio_button = self.window.RecalcFlowrateradioButton

        ValueValidator = QDoubleValidator()
        ValueValidator.setRange(self.value_range.slider_min,
                                self.value_range.slider_max,
                                self.value_range.decimals)

        self.offset_line_edit.setValidator(ValueValidator)
        self.proportion_line_edit.setValidator(ValueValidator)

    # overridden
    def init_line_edit(self):
        self.line_edit = None  # Не нужен, другая логика оператора

    # overridden
    def init_slider(self):
        self.slider = None  # Не нужен, нет слайдера

    # overridden
    def ConnectCallBack(self):
        self.radio_button.toggled.connect(self.RecalcFlowrate)

    # overridden
    def value_changed(self, val):
        pass

    def RecalcFlowrate(self):
        if self.radio_button.isChecked():
            self.model.RecalcFlowrate = True
            self.model.k_flowrate_coefficient = self.line_edit_to_value(self.proportion_line_edit)
            self.model.b_flowrate_coefficient = self.line_edit_to_value(self.offset_line_edit)
        else:
            self.model.RecalcFlowrate = False
            self.model.k_flowrate_coefficient = 1.0
            self.model.b_flowrate_coefficient = 0.0

    @staticmethod
    def line_edit_to_value(line_edit):  # TODO: Есть дублирование кода в таком же методе. Выделить его
        text = line_edit.text()
        if len(text) == 0:
            return 0
        if ',' in text:
            return float(text.replace(',', '.'))
        else:
            return float(text)

