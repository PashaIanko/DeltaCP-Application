from CallBackOperator import CallBackOperator
from SignalGenerationPackage.EdgeSignal.EdgeSignalUIParameters import EdgeSignalUIParameters as UIParameters


class HighLevelFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UIParameters.HighLevelFrequencySliderMin,
            validator_max=UIParameters.HighLevelFrequencySliderMax,
            validator_accuracy=UIParameters.HighLevelFrequencyLineEditAccuracy,
            line_edit=window.HighLevelFrequencylineEdit,
            slider_min=UIParameters.HighLevelFrequencySliderMin,
            slider_max=UIParameters.HighLevelFrequencySliderMax,
            slider=window.HighLevelFrequencyhorizontalSlider,
            update_slider_func=self.update_high_level_freq_slider,
            update_line_edit_func=self.update_high_level_freq_line_edit
        )

    def update_high_level_freq_slider(self):
        self.update_slider(
            line_edit=self.window.HighLevelFrequencylineEdit,
            slider=self.window.HighLevelFrequencyhorizontalSlider,
            calc_constant=UIParameters.HighLevelFrequencyCalcConstant
        )

    def update_high_level_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.HighLevelFrequencylineEdit,
            slider=self.window.HighLevelFrequencyhorizontalSlider,
            calc_constant=UIParameters.HighLevelFrequencyCalcConstant,
            update_model_func=self.update_high_level_freq
        )

    def update_high_level_freq(self, val):
        self.model.HighLevelFrequency = val