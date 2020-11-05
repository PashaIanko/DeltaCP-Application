from CallBackOperator import CallBackOperator
from PyQt5.QtWidgets import QFileDialog, QWidget
import pandas as pd

class AutoFillCallBackOperator(CallBackOperator):
    def __init__(self):
        super().__init__()
        self.configs_path = ".\\SignalGenerationConfigs\\UserSignalConfigs\\SignalConfigs.xlsx"
        self.configs_data = pd.read_excel(self.configs_path)
        self.configs_data.index = self.configs_data['Config Name']

    def ConnectCallBack(self, window):
        self.window = window
        window.AutoFillpushButton.clicked.connect(self.AutoFill)


    def AutoFill(self):
        config_name = self.window.ConfigFileNamelineEdit.text()
        try:
            config_params = self.configs_data.loc[config_name]
            self.set_signal_parameters(
                    [config_params['Start Time'], self.window.StartTimelineEdit],
                    [config_params['Acceleration Time'], self.window.AccelerationTimelineEdit],
                    [config_params['Plateau Time'], self.window.PlateauTimelineEdit],
                    [config_params['Deceleration Time'], self.window.DecelerationTimelineEdit],
                    [config_params['Low Level Frequency'], self.window.LowLevelFrequencylineEdit],
                    [config_params['High Level Frequency'], self.window.HighLevelFrequencylineEdit],
                    [config_params['Vertical Offset'], self.window.VerticalOffsetlineEdit],
                    [config_params['Points Number'], self.window.PointsNumberlineEdit],
                    [config_params['End Time'], self.window.EndTimelineEdit]
            )
        except:
            import sys
            print(sys.exc_info())
            
    def set_signal_parameters(self, *value_widget_pairs):
        for pair in value_widget_pairs:
            value_to_set = pair[0]
            widget = pair[1]

            print(f'value to set = {value_to_set}, type = {type(value_to_set)}')
            #widget.setValue(value_to_set)
            widget.setText(str(value_to_set).replace('.', ','))
            


