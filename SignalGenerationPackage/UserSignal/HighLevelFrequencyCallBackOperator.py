from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters


class HighLevelFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.HighLevelFrequencySliderMin,
            validator_max=UserSignalUIParameters.HighLevelFrequencySliderMax,
            validator_accuracy=UserSignalUIParameters.HighLevelFrequencyLineEditAccuracy,
            line_edit=window.HighLevelFrequencylineEdit,
            slider_min=UserSignalUIParameters.HighLevelFrequencySliderMin,
            slider_max=UserSignalUIParameters.HighLevelFrequencySliderMax,
            slider=window.HighLevelFrequencyhorizontalSlider,
            update_slider_func=self.update_high_level_freq_slider,
            update_line_edit_func=self.update_high_level_freq_line_edit
        )

    def update_high_level_freq_slider(self):
        self.update_slider(
            line_edit=self.window.HighLevelFrequencylineEdit,
            slider=self.window.HighLevelFrequencyhorizontalSlider,
            calc_constant=UserSignalUIParameters.HighLevelFrequencyCalcConstant
        )

    def update_high_level_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.HighLevelFrequencylineEdit,
            slider=self.window.HighLevelFrequencyhorizontalSlider,
            calc_constant=UserSignalUIParameters.HighLevelFrequencyCalcConstant,
            update_model_func=self.update_high_level_freq
        )

    def update_high_level_freq(self, val):
        self.Model.HighLevelFrequency = val