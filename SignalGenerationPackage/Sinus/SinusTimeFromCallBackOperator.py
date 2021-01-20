from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from sys import exc_info
from LoggersConfig import loggers


class SinusTimeFromCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=SinusUIParameters.TimeFromSliderMin,
            validator_max=SinusUIParameters.TimeFromSliderMax,
            validator_accuracy=SinusUIParameters.TimeFromLineEditAccuracy,
            line_edit=self.window.TimeFromlineEdit,
            slider_min=SinusUIParameters.TimeFromSliderMin,
            slider_max=SinusUIParameters.TimeFromSliderMax,
            slider=self.window.horizontalSliderTimeFrom,
            update_slider_func=self.update_time_from_slider,
            update_line_edit_func=self.update_time_from_line_edit
        )

    def update_time_from_slider(self):
        try:
            self.update_slider(
                line_edit=self.window.TimeFromlineEdit,
                slider=self.window.horizontalSliderTimeFrom,
                calc_constant=SinusUIParameters.TimeFromCalcConstant
            )
        except:
            loggers['Debug'].debug(f'Exception in SinusTimeFromCallBackOperator: {exc_info()}')

    def update_time_from_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.TimeFromlineEdit,
                slider=self.window.horizontalSliderTimeFrom,
                calc_constant=SinusUIParameters.TimeFromCalcConstant,
                update_model_func=self.update_time_from
            )
        except:
            loggers['Debug'].debug(f'Exception in SinusTimeFromCallBackOperator: {exc_info()}')

    def update_time_from(self, val):
        self.model.X_from = val
