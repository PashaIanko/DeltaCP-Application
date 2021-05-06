

class ScheduleAutoFillOperator:
    def __init__(self, window, param_names, model, configs_folder):
        self.window = window
        self.param_names = param_names
        self.model = model
        self.configs_folder = configs_folder
        self.config_line_edit = self.window.ConfigFileNamelineEdit


    def ConnectCallBack(self):
        self.window.AutoFillpushButton.clicked.connect(self.AutoFill)

    def AutoFill(self):
        pass