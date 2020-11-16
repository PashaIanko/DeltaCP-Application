from CallBackOperator import CallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters

class EndTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=DynamicPointsDensityUIParameters.EndTimeSliderMin,
            validator_max=DynamicPointsDensityUIParameters.EndTimeSliderMax,
            validator_accuracy=DynamicPointsDensityUIParameters.EndTimeLineEditAccuracy,
            line_edit=window.EndTimelineEdit,
            slider_min=DynamicPointsDensityUIParameters.EndTimeSliderMin,
            slider_max=DynamicPointsDensityUIParameters.EndTimeSliderMax,
            slider=window.EndTimehorizontalSlider,
            update_slider_func=self.update_end_time_slider,
            update_line_edit_func=self.update_end_time_line_edit
        )

    def update_end_time_slider(self):
        self.update_slider(
            line_edit=self.window.EndTimelineEdit,
            slider=self.window.EndTimehorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.EndTimeCalcConstant
        )

    def update_end_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.EndTimelineEdit,
            slider=self.window.EndTimehorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.EndTimeCalcConstant,
            update_model_func=self.update_end_time
        )

    def update_end_time(self, val):
        self.Model.EndTime = val