from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from sys import exc_info

class SinusAmplitudeCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=SinusUIParameters.AmplitudeSliderMin,
            validator_max=SinusUIParameters.AmplitudeSliderMax,
            validator_accuracy=SinusUIParameters.AmplitudeLineEditAccuracy,
            line_edit=self.window.AmplitudelineEdit,
            slider_min=SinusUIParameters.AmplitudeSliderMin,
            slider_max=SinusUIParameters.AmplitudeSliderMax,
            slider=self.window.horizontalSliderAmplitude,
            update_slider_func=self.update_amplitude_slider,
            update_line_edit_func=self.update_amplitude_line_edit
        )

    def update_amplitude_slider(self):
        try:
            self.update_slider(
                line_edit=self.window.AmplitudelineEdit,
                slider=self.window.horizontalSliderAmplitude,
                calc_constant=SinusUIParameters.AmplitudeCalcConstant
            )
        except:
            print(exc_info())

    def update_amplitude_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.AmplitudelineEdit,
                slider=self.window.horizontalSliderAmplitude,
                calc_constant=SinusUIParameters.AmplitudeCalcConstant,
                update_model_func=self.update_amplitude
            )
        except:
            print(exc_info())

    def update_amplitude(self, val):
        self.model.amplitude = val