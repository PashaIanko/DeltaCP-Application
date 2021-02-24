from CallBackOperator import CallBackOperator
from SignalGenerationPackage.EdgeSignal.EdgeSignalUIParameters import EdgeSignalUIParameters as UIParameters


class DecelerationTimeCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UIParameters.DecelerationTimeSliderMin,
            validator_max=UIParameters.DecelerationTimeSliderMax,
            validator_accuracy=UIParameters.DecelerationTimeLineEditAccuracy,
            line_edit=window.DecelerationTimelineEdit,
            slider_min=UIParameters.DecelerationTimeSliderMin,
            slider_max=UIParameters.DecelerationTimeSliderMax,
            slider=window.DecelerationTimehorizontalSlider,
            update_slider_func=self.update_deceleration_time_slider,
            update_line_edit_func=self.update_deceleration_time_line_edit
        )

    def update_deceleration_time_slider(self):
        self.update_slider(
            line_edit=self.window.DecelerationTimelineEdit,
            slider=self.window.DecelerationTimehorizontalSlider,
            calc_constant=UIParameters.DecelerationTimeCalcConstant
        )

    def update_deceleration_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.DecelerationTimelineEdit,
            slider=self.window.DecelerationTimehorizontalSlider,
            calc_constant=UIParameters.DecelerationTimeCalcConstant,
            update_model_func=self.update_deceleration_time
        )

    def update_deceleration_time(self, val):
        self.model.DecelerationTime = val