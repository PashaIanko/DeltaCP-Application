# Небольшая структура для упрощения
# кода по синхронизации слайдеров и line_edt виджетов

class SliderTextPair:
    def __init__(self, slider, line_edit, calc_constant):
        self.slider = slider
        self.line_edit = line_edit
        self.calc_constant = calc_constant

