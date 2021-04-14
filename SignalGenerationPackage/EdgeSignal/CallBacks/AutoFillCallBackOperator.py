from AutoFillOperator import AutoFillOperator


class AutoFillCallBackOperator(AutoFillOperator):
    def __init__(self, window, param_names, line_edits, sliders, model):
        super().__init__(
            window,
            param_names,
            line_edits,
            sliders,
            model,
            configs_path=".\\SignalGenerationConfigs\\EdgeSignalConfigs\\SignalConfigs.xlsx")

    def ConnectCallBack(self):
        self.window.AutoFillpushButton.clicked.connect(self.AutoFill)
        self.window.SavePresetpushButton.clicked.connect(self.SavePreset)
        self.window.DeletePresetpushButton.clicked.connect(self.DeletePreset)

    def get_config_name(self):
        return self.window.ConfigFileNamelineEdit.text()