from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters
from AutoFillOperator import AutoFillOperator


class AutoFillCallBackOperator(AutoFillOperator):
    def __init__(self, model):
        super().__init__(model,
                         configs_path=".\\SignalGenerationConfigs\\DynamicPointsDensitySignalConfigs\\SignalConfigs.xlsx")

    def ConnectCallBack(self, window):
        self.window = window
        window.AutoFillpushButton.clicked.connect(self.AutoFill)

    def get_config_name(self):
        return self.window.ConfigFileNamelineEdit.text()

    def init_autofill_parameters(self):
        window = self.window
        self.autofill_parameters = [
                    [self.config_params['Start Time'],           DynamicPointsDensityUIParameters.StartTimeCalcConstant,           window.StartTimehorizontalSlider],
                    [self.config_params['Acceleration Time'],    DynamicPointsDensityUIParameters.AccelerationTimeCalcConstant,    window.AccelerationTimehorizontalSlider],
                    [self.config_params['Plateau Time'],         DynamicPointsDensityUIParameters.PlateauTimeCalcConstant,         window.PlateauTimehorizontalSlider],
                    [self.config_params['Deceleration Time'],    DynamicPointsDensityUIParameters.DecelerationTimeCalcConstant,    window.DecelerationTimehorizontalSlider],
                    [self.config_params['Low Level Frequency'],  DynamicPointsDensityUIParameters.LowLevelFrequencyCalcConstant,   window.LowLevelFrequencyhorizontalSlider],
                    [self.config_params['High Level Frequency'], DynamicPointsDensityUIParameters.HighLevelFrequencyCalcConstant,  window.HighLevelFrequencyhorizontalSlider],
                    #[self.config_params['Vertical Offset'],      DynamicPointsDensityUIParameters.VerticalOffsetCalcConstant,      window.VerticalOffsethorizontalSlider],
                    [self.config_params['Points Density'],       DynamicPointsDensityUIParameters.PointsDensityCalcConstant,       window.PointsDensityhorizontalSlider],
                    [self.config_params['End Time'],             DynamicPointsDensityUIParameters.EndTimeCalcConstant,             window.EndTimehorizontalSlider]
                ]