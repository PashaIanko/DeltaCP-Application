from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters

class RequestFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=SinusUIParameters.RequestFreqSliderMin,
            validator_max=SinusUIParameters.RequestFreqSliderMax,
            validator_accuracy=SinusUIParameters.RequestFreqLineEditAccuracy,
            line_edit=self.window.RequestFrequencylineEdit,
            slider_min=SinusUIParameters.RequestFreqSliderMin,
            slider_max=SinusUIParameters.RequestFreqSliderMax,
            slider=self.window.horizontalSliderRequestFrequency,
            update_slider_func=self.update_request_freq_slider,
            update_line_edit_func=self.update_request_freq_line_edit
        )

    def update_request_freq_slider(self):
        self.update_slider(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.horizontalSliderRequestFrequency,
            calc_constant=SinusUIParameters.RequestFreqCalcConstant
        )

    def update_request_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.horizontalSliderRequestFrequency,
            calc_constant=SinusUIParameters.RequestFreqCalcConstant,
            update_model_func=self.update_request_freq
        )

    def update_request_freq(self, val):
        self.model.request_freq = val