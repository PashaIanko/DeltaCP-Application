from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters


class StartTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=          UserSignalUIParameters.StartTimeSliderMin,
            validator_max=          UserSignalUIParameters.StartTimeSliderMax,
            validator_accuracy=     UserSignalUIParameters.StartTimeLineEditAccuracy,
            line_edit=              window.StartTimelineEdit,
            slider_min=             UserSignalUIParameters.StartTimeSliderMin,
            slider_max=             UserSignalUIParameters.StartTimeSliderMax,
            slider=                 window.StartTimehorizontalSlider,
            update_slider_func=     self.update_start_time_slider,
            update_line_edit_func=  self.update_start_time_line_edit
        )

    def update_start_time_slider(self):
        self.update_slider(
            line_edit=self.window.StartTimelineEdit,
            slider=self.window.StartTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.StartTimeCalcConstant
        )

    def update_start_time_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.StartTimelineEdit,
                slider=self.window.StartTimehorizontalSlider,
                calc_constant=UserSignalUIParameters.StartTimeCalcConstant,
                update_model_func=self.update_start_time
            )
        except:
            import sys
            print(sys.exc_info())

    def update_start_time(self, val):
        print(f'updating model, now val = {val}')
        self.Model.StartTime = val