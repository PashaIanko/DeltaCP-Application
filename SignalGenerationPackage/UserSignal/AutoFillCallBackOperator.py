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

    # overridden
    def init_param_names_list(self):
        # ВАЖНО - лист параметров, лист констант и лист слайдеров
        # должны объявляться в одинаковом порядке
        self.param_names_list = [
            'Start Time', 'Acceleration Time', 'Plateau Time',
            'Deceleration Time', 'Low Level Frequency', 'High Level Frequency',
            'Vertical Offset', 'Points Number', 'End Time'
        ]

    # overridden
    def init_constants_list(self):
        self.constants_list = [
            UserSignalUIParameters.StartTimeCalcConstant,
            UserSignalUIParameters.AccelerationTimeCalcConstant,
            UserSignalUIParameters.PlateauTimeCalcConstant,
            UserSignalUIParameters.DecelerationTimeCalcConstant,
            UserSignalUIParameters.LowLevelFrequencyCalcConstant,
            UserSignalUIParameters.HighLevelFrequencyCalcConstant,
            UserSignalUIParameters.VerticalOffsetCalcConstant,
            UserSignalUIParameters.PointsNumberCalcConstant,
            UserSignalUIParameters.EndTimeCalcConstant
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
            self.window.VerticalOffsethorizontalSlider,
            self.window.PointsNumberhorizontalSlider,
            self.window.EndTimehorizontalSlider,
        ]