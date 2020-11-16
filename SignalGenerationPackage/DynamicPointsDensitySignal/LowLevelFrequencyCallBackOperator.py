from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters


class LowLevelFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

        # overriden

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.LowLevelFrequencySliderMin,
            validator_max=UserSignalUIParameters.LowLevelFrequencySliderMax,
            validator_accuracy=UserSignalUIParameters.LowLevelFrequencyLineEditAccuracy,
            line_edit=window.LowLevelFrequencylineEdit,
            slider_min=UserSignalUIParameters.LowLevelFrequencySliderMin,
            slider_max=UserSignalUIParameters.LowLevelFrequencySliderMax,
            slider=window.LowLevelFrequencyhorizontalSlider,
            update_slider_func=self.update_low_level_freq_slider,
            update_line_edit_func=self.update_low_level_freq_line_edit
        )

    def update_low_level_freq_slider(self):
        self.update_slider(
            line_edit=self.window.LowLevelFrequencylineEdit,
            slider=self.window.LowLevelFrequencyhorizontalSlider,
            calc_constant=UserSignalUIParameters.LowLevelFrequencyCalcConstant
        )

    def update_low_level_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.LowLevelFrequencylineEdit,
            slider=self.window.LowLevelFrequencyhorizontalSlider,
            calc_constant=UserSignalUIParameters.LowLevelFrequencyCalcConstant,
            update_model_func=self.update_low_level_freq
        )

    def update_low_level_freq(self, val):
        self.Model.LowLevelFrequency = val