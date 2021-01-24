from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters
from CallBackOperator import CallBackOperator
import pandas as pd



class AutoFillCallBackOperator(CallBackOperator):
    def __init__(self, model):
        super().__init__(model)  # TODO: Выделить интерфейс AutoFill Operator
        self.configs_path = ".\\SignalGenerationConfigs\\DynamicPointsDensitySignalConfigs\\SignalConfigs.xlsx"
        self.configs_data = pd.read_excel(self.configs_path)
        self.configs_data.index = self.configs_data['Config Name']

    def ConnectCallBack(self, window):
        self.window = window
        window.AutoFillpushButton.clicked.connect(self.AutoFill)


    def AutoFill(self):
        config_name = self.window.ConfigFileNamelineEdit.text()
        try:
            config_params = self.configs_data.loc[config_name]
            window = self.window
            self.set_signal_parameters(
                [
                    [config_params['Start Time'],           DynamicPointsDensityUIParameters.StartTimeCalcConstant,           window.StartTimehorizontalSlider],
                    [config_params['Acceleration Time'],    DynamicPointsDensityUIParameters.AccelerationTimeCalcConstant,    window.AccelerationTimehorizontalSlider],
                    [config_params['Plateau Time'],         DynamicPointsDensityUIParameters.PlateauTimeCalcConstant,         window.PlateauTimehorizontalSlider],
                    [config_params['Deceleration Time'],    DynamicPointsDensityUIParameters.DecelerationTimeCalcConstant,    window.DecelerationTimehorizontalSlider],
                    [config_params['Low Level Frequency'],  DynamicPointsDensityUIParameters.LowLevelFrequencyCalcConstant,   window.LowLevelFrequencyhorizontalSlider],
                    [config_params['High Level Frequency'], DynamicPointsDensityUIParameters.HighLevelFrequencyCalcConstant,  window.HighLevelFrequencyhorizontalSlider],
                    [config_params['Vertical Offset'],      DynamicPointsDensityUIParameters.VerticalOffsetCalcConstant,      window.VerticalOffsethorizontalSlider],
                    [config_params['Points Density'],       DynamicPointsDensityUIParameters.PointsDensityCalcConstant,        window.PointsDensityhorizontalSlider],
                    [config_params['End Time'],             DynamicPointsDensityUIParameters.EndTimeCalcConstant,             window.EndTimehorizontalSlider]
                ]
            )
        except:
            import sys
            from LoggersConfig import loggers
            loggers['Debug'].debug(f'AutoFillCallBackOperator: AutoFill: {sys.exc_info()}')

    def set_signal_parameters(self, value_widgets):
        for v in value_widgets:
            value_to_set = v[0]
            constant = v[1]
            slider = v[2]
            slider.setValue(value_to_set * constant)


            


