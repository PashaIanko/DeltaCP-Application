from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters
from AutoFillOperator import AutoFillOperator


class AutoFillCallBackOperator(AutoFillOperator):
    def __init__(self, model):
        super().__init__(model,
                         configs_path=".\\SignalGenerationConfigs\\UserSignalConfigs\\SignalConfigs.xlsx")

    def ConnectCallBack(self, window):
        self.window = window
        window.AutoFillpushButton.clicked.connect(self.AutoFill)

    def get_config_name(self):
        return self.window.ConfigFileNamelineEdit.text()

    def init_autofill_parameters(self):
        window = self.window

        self.autofill_parameters = [
            [self.config_params['Start Time'], UserSignalUIParameters.StartTimeCalcConstant,                    window.StartTimehorizontalSlider],
            [self.config_params['Acceleration Time'], UserSignalUIParameters.AccelerationTimeCalcConstant,      window.AccelerationTimehorizontalSlider],
            [self.config_params['Plateau Time'], UserSignalUIParameters.PlateauTimeCalcConstant,                window.PlateauTimehorizontalSlider],
            [self.config_params['Deceleration Time'], UserSignalUIParameters.DecelerationTimeCalcConstant,      window.DecelerationTimehorizontalSlider],
            [self.config_params['Low Level Frequency'], UserSignalUIParameters.LowLevelFrequencyCalcConstant,   window.LowLevelFrequencyhorizontalSlider],
            [self.config_params['High Level Frequency'], UserSignalUIParameters.HighLevelFrequencyCalcConstant, window.HighLevelFrequencyhorizontalSlider],
            [self.config_params['Vertical Offset'], UserSignalUIParameters.VerticalOffsetCalcConstant,          window.VerticalOffsethorizontalSlider],
            [self.config_params['Points Number'], UserSignalUIParameters.PointsNumberCalcConstant,              window.PointsNumberhorizontalSlider],
            [self.config_params['End Time'], UserSignalUIParameters.EndTimeCalcConstant,                        window.EndTimehorizontalSlider]
        ]