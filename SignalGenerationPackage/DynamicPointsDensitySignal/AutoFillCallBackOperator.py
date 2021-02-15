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

    # overridden
    def init_param_names_list(self):
        # ВАЖНО чтобы param names list, constants list и sliders list шли в том же порядке
        self.param_names_list = [
            'Start Time', 'Acceleration Time', 'Plateau Time', 'Deceleration Time', 'Low Level Frequency',
            'High Level Frequency', 'Points Density', 'End Time']

    # overridden
    def init_constants_list(self):
        self.constants_list = [
            DynamicPointsDensityUIParameters.StartTimeCalcConstant,
            DynamicPointsDensityUIParameters.AccelerationTimeCalcConstant,
            DynamicPointsDensityUIParameters.PlateauTimeCalcConstant,
            DynamicPointsDensityUIParameters.DecelerationTimeCalcConstant,
            DynamicPointsDensityUIParameters.LowLevelFrequencyCalcConstant,
            DynamicPointsDensityUIParameters.HighLevelFrequencyCalcConstant,
            DynamicPointsDensityUIParameters.PointsDensityCalcConstant,
            DynamicPointsDensityUIParameters.EndTimeCalcConstant,
        ]

    # overridden
    def init_sliders_list(self):
        self.sliders_list = [
            self.window.StartTimehorizontalSlider,
            self.window.AccelerationTimehorizontalSlider,
            self.window.PlateauTimehorizontalSlider,
            self.window.DecelerationTimehorizontalSlider,
            self.window.LowLevelFrequencyhorizontalSlider,
            self.window.HighLevelFrequencyhorizontalSlider,
            self.window.PointsDensityhorizontalSlider,
            self.window.EndTimehorizontalSlider
        ]

