from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from sys import exc_info


class SinusTimeToCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=SinusUIParameters.TimeToSliderMin,
            validator_max=SinusUIParameters.TimeToSliderMax,
            validator_accuracy=SinusUIParameters.TimeToLineEditAccuracy,
            line_edit=self.window.TimeTolineEdit,
            slider_min=SinusUIParameters.TimeToSliderMin,
            slider_max=SinusUIParameters.TimeToSliderMax,
            slider=self.window.horizontalSliderTimeTo,
            update_slider_func=self.update_time_to_slider,
            update_line_edit_func=self.update_time_to_line_edit
        )

    def update_time_to_slider(self):
        try:
            self.update_slider(
                line_edit=self.window.TimeTolineEdit,
                slider=self.window.horizontalSliderTimeTo,
                calc_constant=SinusUIParameters.TimeToCalcConstant
            )
        except:
            print(exc_info())

    def update_time_to_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.TimeTolineEdit,
                slider=self.window.horizontalSliderTimeTo,
                calc_constant=SinusUIParameters.TimeToCalcConstant,
                update_model_func=self.update_time_to
            )
        except:
            print(exc_info())

    def update_time_to(self, val):
        self.model.X_to = val