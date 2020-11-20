from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters

class EndTimeCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.EndTimeSliderMin,
            validator_max=UserSignalUIParameters.EndTimeSliderMax,
            validator_accuracy=UserSignalUIParameters.EndTimeLineEditAccuracy,
            line_edit=window.EndTimelineEdit,
            slider_min=UserSignalUIParameters.EndTimeSliderMin,
            slider_max=UserSignalUIParameters.EndTimeSliderMax,
            slider=window.EndTimehorizontalSlider,
            update_slider_func=self.update_end_time_slider,
            update_line_edit_func=self.update_end_time_line_edit
        )

    def update_end_time_slider(self):
        self.update_slider(
            line_edit=self.window.EndTimelineEdit,
            slider=self.window.EndTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.EndTimeCalcConstant
        )

    def update_end_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.EndTimelineEdit,
            slider=self.window.EndTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.EndTimeCalcConstant,
            update_model_func=self.update_end_time
        )

    def update_end_time(self, val):
        self.model.EndTime = val