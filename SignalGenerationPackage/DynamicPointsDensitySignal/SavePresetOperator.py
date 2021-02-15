from CallBackOperator import CallBackOperator


class SavePresetOperator(CallBackOperator):
    def __init__(self, slider_constants, sliders, param_names):
        super().__init__()
        self.slider_consts = slider_constants
        self.sliders = sliders
        self.param_names = param_names  # На этом этапе, константы, слайдеры и
                                        # названия параметров в ОДНОМ ПОРЯДКЕ.

    # overridden
    def ConnectCallBack(self, window):
        self.window = window
        window.SavePresetpushButton.clicked.connect(self.SavePreset)

    def SavePreset(self):
        pass