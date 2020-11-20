from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters

class AccelerationTimeCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=          UserSignalUIParameters.AccelerationTimeSliderMin,
            validator_max=          UserSignalUIParameters.AccelerationTimeSliderMax,
            validator_accuracy=     UserSignalUIParameters.AccelerationTimeLineEditAccuracy,
            line_edit=              window.AccelerationTimelineEdit,
            slider_min=             UserSignalUIParameters.AccelerationTimeSliderMin,
            slider_max=             UserSignalUIParameters.AccelerationTimeSliderMax,
            slider=                 window.AccelerationTimehorizontalSlider,
            update_slider_func=     self.update_acceleration_time_slider,
            update_line_edit_func=  self.update_acceleration_time_line_edit
        )

    def update_acceleration_time_slider(self):
        self.update_slider(
            line_edit=self.window.AccelerationTimelineEdit,
            slider=self.window.AccelerationTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.AccelerationTimeCalcConstant
        )

    def update_acceleration_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.AccelerationTimelineEdit,
            slider=self.window.AccelerationTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.AccelerationTimeCalcConstant,
            update_model_func=self.update_acceleration_time
        )

    def update_acceleration_time(self, val):
        self.model.AccelerationTime = val
