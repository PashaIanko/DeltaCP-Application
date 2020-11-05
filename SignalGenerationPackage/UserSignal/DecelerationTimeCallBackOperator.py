from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters
import sys


class DecelerationTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.DecelerationTimeSliderMin,
            validator_max=UserSignalUIParameters.DecelerationTimeSliderMax,
            validator_accuracy=UserSignalUIParameters.DecelerationTimeLineEditAccuracy,
            line_edit=window.DecelerationTimelineEdit,
            slider_min=UserSignalUIParameters.DecelerationTimeSliderMin,
            slider_max=UserSignalUIParameters.DecelerationTimeSliderMax,
            slider=window.DecelerationTimehorizontalSlider,
            update_slider_func=self.update_deceleration_time_slider,
            update_line_edit_func=self.update_deceleration_time_line_edit
        )

    def update_deceleration_time_slider(self):
        self.update_slider(
            line_edit=self.window.DecelerationTimelineEdit,
            slider=self.window.DecelerationTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.DecelerationTimeCalcConstant
        )

    def update_deceleration_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.DecelerationTimelineEdit,
            slider=self.window.DecelerationTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.DecelerationTimeCalcConstant,
            update_model_func=self.update_deceleration_time
        )

    def update_deceleration_time(self, val):
        self.Model.DecelerationTime = val