from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters

class RequestFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.RequestFreqSliderMin,
            validator_max=UserSignalUIParameters.RequestFreqSliderMax,
            validator_accuracy=UserSignalUIParameters.RequestFreqLineEditAccuracy,
            line_edit=self.window.RequestFrequencylineEdit,
            slider_min=UserSignalUIParameters.RequestFreqSliderMin,
            slider_max=UserSignalUIParameters.RequestFreqSliderMax,
            slider=self.window.RequestFrequencyhorizontalSlider,
            update_slider_func=self.update_request_freq_slider,
            update_line_edit_func=self.update_request_freq_line_edit
        )

    def update_request_freq_slider(self):
        self.update_slider(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.RequestFrequencyhorizontalSlider,
            calc_constant=UserSignalUIParameters.RequestFreqCalcConstant
        )

    def update_request_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.RequestFrequencyhorizontalSlider,
            calc_constant=UserSignalUIParameters.RequestFreqCalcConstant,
            update_model_func=self.update_request_freq
        )

    def update_request_freq(self, val):
        self.model.request_freq = val