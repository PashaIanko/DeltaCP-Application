from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from sys import exc_info

class SinusOmegaCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=SinusUIParameters.OmegaSliderMin,
            validator_max=SinusUIParameters.OmegaSliderMax,
            validator_accuracy=SinusUIParameters.OmegaLineEditAccuracy,
            line_edit=self.window.OmegalineEdit,
            slider_min=SinusUIParameters.OmegaSliderMin,
            slider_max=SinusUIParameters.OmegaSliderMax,
            slider=self.window.horizontalSliderOmega,
            update_slider_func=self.update_omega_slider,
            update_line_edit_func=self.update_omega_line_edit
        )

    def update_omega_slider(self):
        try:
            self.update_slider(
                line_edit=self.window.OmegalineEdit,
                slider=self.window.horizontalSliderOmega,
                calc_constant=SinusUIParameters.OmegaCalcConstant
            )
        except:
            print(exc_info())

    def update_omega_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.OmegalineEdit,
                slider=self.window.horizontalSliderOmega,
                calc_constant=SinusUIParameters.OmegaCalcConstant,
                update_model_func=self.update_omega
            )
        except:
            print(exc_info())

    def update_omega(self, val):
        self.model.omega = val