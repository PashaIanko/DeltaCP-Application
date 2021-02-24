from CallBackOperator import CallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters

class RequestFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=DynamicPointsDensityUIParameters.RequestFreqSliderMin,
            validator_max=DynamicPointsDensityUIParameters.RequestFreqSliderMax,
            validator_accuracy=DynamicPointsDensityUIParameters.RequestFreqLineEditAccuracy,
            line_edit=self.window.RequestFrequencylineEdit,
            slider_min=DynamicPointsDensityUIParameters.RequestFreqSliderMin,
            slider_max=DynamicPointsDensityUIParameters.RequestFreqSliderMax,
            slider=self.window.RequestFrequencyhorizontalSlider,
            update_slider_func=self.update_request_freq_slider,
            update_line_edit_func=self.update_request_freq_line_edit
        )

    def update_request_freq_slider(self):
        self.update_slider(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.RequestFrequencyhorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.RequestFreqCalcConstant
        )

    def update_request_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.RequestFrequencyhorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.RequestFreqCalcConstant,
            update_model_func=self.update_request_freq
        )

    def update_request_freq(self, val):
        self.model.request_freq = val