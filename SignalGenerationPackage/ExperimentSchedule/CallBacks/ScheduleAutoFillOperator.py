import pandas as pd
from PopUpNotifier.PopUpNotifier import PopUpNotifier


class ScheduleAutoFillOperator:
    def __init__(self, window, param_names, model, configs_folder):
        self.window = window
        self.param_names = param_names
        self.model = model
        self.configs_folder = configs_folder
        self.config_line_edit = self.window.ConfigFileNamelineEdit


    def ConnectCallBack(self):
        self.window.AutoFillpushButton.clicked.connect(self.AutoFill)

    def check_data_validity(self, configs_df):
        column_names = configs_df.columns
        absent_columns = []
        for p in self.param_names:
            if not (p in column_names):
                absent_columns.append(p)
        return absent_columns


    def AutoFill(self):
        config_name = self.config_line_edit.text()
        config_filepath = self.configs_folder + config_name + '.xlsx'
        configs_df = pd.read_excel(config_filepath)

        absent_columns = self.check_data_validity(configs_df)
        if len(absent_columns) == 0:
            # Значит, все необходимые колонки
            # были заполнены, данные правильные
            frequencies = configs_df['Frequencies'].values
            seconds = configs_df['Seconds'].values
            request_freq = configs_df['Request every N seconds'].values[0]

            self.model.frequencies = frequencies
            self.model.seconds = seconds
            self.model.request_every_N_sec = request_freq

        else:
            PopUpNotifier.Error(
                f'Missing Columns in file "{config_name}":\n{absent_columns}'
            )

        # Закроем файл
        del configs_df
