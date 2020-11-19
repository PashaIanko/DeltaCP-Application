from CallBackOperator import CallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters


class LowLevelFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=DynamicPointsDensityUIParameters.LowLevelFrequencySliderMin,
            validator_max=DynamicPointsDensityUIParameters.LowLevelFrequencySliderMax,
            validator_accuracy=DynamicPointsDensityUIParameters.LowLevelFrequencyLineEditAccuracy,
            line_edit=window.LowLevelFrequencylineEdit,
            slider_min=DynamicPointsDensityUIParameters.LowLevelFrequencySliderMin,
            slider_max=DynamicPointsDensityUIParameters.LowLevelFrequencySliderMax,
            slider=window.LowLevelFrequencyhorizontalSlider,
            update_slider_func=self.update_low_level_freq_slider,
            update_line_edit_func=self.update_low_level_freq_line_edit
        )

    def update_low_level_freq_slider(self):
        self.update_slider(
            line_edit=self.window.LowLevelFrequencylineEdit,
            slider=self.window.LowLevelFrequencyhorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.LowLevelFrequencyCalcConstant
        )

    def update_low_level_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.LowLevelFrequencylineEdit,
            slider=self.window.LowLevelFrequencyhorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.LowLevelFrequencyCalcConstant,
            update_model_func=self.update_low_level_freq
        )

    def update_low_level_freq(self, val):
        self.model.LowLevelFrequency = val