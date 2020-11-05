from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters


class PlateauTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.PlateauTimeSliderMin,
            validator_max=UserSignalUIParameters.PlateauTimeSliderMax,
            validator_accuracy=UserSignalUIParameters.PlateauTimeLineEditAccuracy,
            line_edit=window.PlateauTimelineEdit,
            slider_min=UserSignalUIParameters.PlateauTimeSliderMin,
            slider_max=UserSignalUIParameters.PlateauTimeSliderMax,
            slider=window.PlateauTimehorizontalSlider,
            update_slider_func=self.update_plateau_time_slider,
            update_line_edit_func=self.update_plateau_time_line_edit
        )

    def update_plateau_time_slider(self):
        self.update_slider(
            line_edit=self.window.PlateauTimelineEdit,
            slider=self.window.PlateauTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.PlateauTimeCalcConstant
        )

    def update_plateau_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.PlateauTimelineEdit,
            slider=self.window.PlateauTimehorizontalSlider,
            calc_constant=UserSignalUIParameters.PlateauTimeCalcConstant,
            update_model_func=self.update_Plateau_time
        )

    def update_plateau_time(self, val):
        print(f'updating model, now val = {val}')
        self.Model.PlateauTime = val