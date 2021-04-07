from CallBackOperator import CallBackOperator
from SignalGenerationPackage.EdgeSignal.EdgeSignalUIParameters import EdgeSignalUIParameters as UIParameters

class RequestFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, main_window, model):
        super().__init__(window=main_window, model=model, value_range=None)

    def ConnectCallBack(self):

        self.setup_callback_and_synchronize_slider(
            validator_min=UIParameters.RequestFreqSliderMin,
            validator_max=UIParameters.RequestFreqSliderMax,
            validator_accuracy=UIParameters.RequestFreqLineEditAccuracy,
            line_edit=self.window.RequestFrequencylineEdit,
            slider_min=UIParameters.RequestFreqSliderMin,
            slider_max=UIParameters.RequestFreqSliderMax,
            slider=self.window.RequestFrequencyhorizontalSlider,
            update_slider_func=self.update_request_freq_slider,
            update_line_edit_func=self.update_request_freq_line_edit
        )

    def update_request_freq_slider(self):
        self.update_slider(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.RequestFrequencyhorizontalSlider,
            calc_constant=UIParameters.RequestFreqCalcConstant
        )

    def update_request_freq_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.RequestFrequencylineEdit,
            slider=self.window.RequestFrequencyhorizontalSlider,
            calc_constant=UIParameters.RequestFreqCalcConstant,
            update_model_func=self.update_request_freq
        )

    def update_request_freq(self, val):
        self.model.request_freq = val

    # overridden
    def init_slider(self):
        pass

    # overridden
    def init_line_edit(self):
        pass

    # overridden
    def value_changed(self, val):
        pass