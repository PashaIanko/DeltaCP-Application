from CallBackOperator import CallBackOperator
from SignalGenerationPackage.EdgeSignal.EdgeSignalUIParameters import EdgeSignalUIParameters as UIParameters


class StartTimeCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=          UIParameters.StartTimeSliderMin,
            validator_max=          UIParameters.StartTimeSliderMax,
            validator_accuracy=     UIParameters.StartTimeLineEditAccuracy,
            line_edit=              window.StartTimelineEdit,
            slider_min=             UIParameters.StartTimeSliderMin,
            slider_max=             UIParameters.StartTimeSliderMax,
            slider=                 window.StartTimehorizontalSlider,
            update_slider_func=     self.update_start_time_slider,
            update_line_edit_func=  self.update_start_time_line_edit
        )

    def update_start_time_slider(self):
        self.update_slider(
            line_edit=self.window.StartTimelineEdit,
            slider=self.window.StartTimehorizontalSlider,
            calc_constant=UIParameters.StartTimeCalcConstant
        )

    def update_start_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.StartTimelineEdit,
            slider=self.window.StartTimehorizontalSlider,
            calc_constant=UIParameters.StartTimeCalcConstant,
            update_model_func=self.update_start_time
        )

    def update_start_time(self, val):
        self.model.StartTime = val