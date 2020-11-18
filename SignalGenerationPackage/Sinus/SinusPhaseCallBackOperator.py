from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from sys import exc_info


class SinusPhaseCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=SinusUIParameters.PhaseSliderMin,
            validator_max=SinusUIParameters.PhaseSliderMax,
            validator_accuracy=SinusUIParameters.PhaseLineEditAccuracy,
            line_edit=self.window.PhaselineEdit,
            slider_min=SinusUIParameters.PhaseSliderMin,
            slider_max=SinusUIParameters.PhaseSliderMax,
            slider=self.window.horizontalSliderPhase,
            update_slider_func=self.update_phase_slider,
            update_line_edit_func=self.update_phase_line_edit
        )

    def update_phase_slider(self):
        try:
            self.update_slider(
                line_edit=self.window.PhaselineEdit,
                slider=self.window.horizontalSliderPhase,
                calc_constant=SinusUIParameters.PhaseCalcConstant
            )
        except:
            print(exc_info())

    def update_phase_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.PhaselineEdit,
                slider=self.window.horizontalSliderPhase,
                calc_constant=SinusUIParameters.PhaseCalcConstant,
                update_model_func=self.update_phase
            )
        except:
            print(exc_info())

    def update_phase(self, val):
        self.model.phase = val