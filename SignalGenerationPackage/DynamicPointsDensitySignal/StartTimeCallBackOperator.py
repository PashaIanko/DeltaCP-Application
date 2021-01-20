from CallBackOperator import CallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters


class StartTimeCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=          DynamicPointsDensityUIParameters.StartTimeSliderMin,
            validator_max=          DynamicPointsDensityUIParameters.StartTimeSliderMax,
            validator_accuracy=     DynamicPointsDensityUIParameters.StartTimeLineEditAccuracy,
            line_edit=              window.StartTimelineEdit,
            slider_min=             DynamicPointsDensityUIParameters.StartTimeSliderMin,
            slider_max=             DynamicPointsDensityUIParameters.StartTimeSliderMax,
            slider=                 window.StartTimehorizontalSlider,
            update_slider_func=     self.update_start_time_slider,
            update_line_edit_func=  self.update_start_time_line_edit
        )

    def update_start_time_slider(self):
        self.update_slider(
            line_edit=self.window.StartTimelineEdit,
            slider=self.window.StartTimehorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.StartTimeCalcConstant
        )

    def update_start_time_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.StartTimelineEdit,
                slider=self.window.StartTimehorizontalSlider,
                calc_constant=DynamicPointsDensityUIParameters.StartTimeCalcConstant,
                update_model_func=self.update_start_time
            )
        except:
            import sys
            from LoggersConfig import loggers
            loggers['Debug'].debug(f'StartTimeCallBackOperator: {sys.exc_info()}')

    def update_start_time(self, val):
        self.model.StartTime = val