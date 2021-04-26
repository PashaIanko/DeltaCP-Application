from AutoFillOperator import AutoFillOperator


class AutoFillCallBackOperator(AutoFillOperator):
    def __init__(self, slider_constants, param_names, sliders, model):
        super().__init__(
            slider_constants,
            param_names,
            sliders,
            model,
            configs_path=".\\SignalGenerationConfigs\\UserSignalConfigs\\SignalConfigs.xlsx")

    # overridden
    def ConnectCallBack(self, window):
        self.window = window
        window.AutoFillpushButton.clicked.connect(self.AutoFill)
        window.SavePresetpushButton.clicked.connect(self.SavePreset)
        window.DeletePresetpushButton.clicked.connect(self.DeletePreset)

    # overridden
    def init_config_line_edit(self):
        self.config_line_edit = self.window.ConfigFileNamelineEdit
