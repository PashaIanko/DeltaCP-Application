from CallBackOperator import CallBackOperator
from SignalGenerationPackage.EdgeSignal.EdgeSignalUIParameters import EdgeSignalUIParameters as UIParameters


class PlateauTimeCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UIParameters.PlateauTimeSliderMin,
            validator_max=UIParameters.PlateauTimeSliderMax,
            validator_accuracy=UIParameters.PlateauTimeLineEditAccuracy,
            line_edit=window.PlateauTimelineEdit,
            slider_min=UIParameters.PlateauTimeSliderMin,
            slider_max=UIParameters.PlateauTimeSliderMax,
            slider=window.PlateauTimehorizontalSlider,
            update_slider_func=self.update_plateau_time_slider,
            update_line_edit_func=self.update_plateau_time_line_edit
        )

    def update_plateau_time_slider(self):
        self.update_slider(
            line_edit=self.window.PlateauTimelineEdit,
            slider=self.window.PlateauTimehorizontalSlider,
            calc_constant=UIParameters.PlateauTimeCalcConstant
        )

    def update_plateau_time_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.PlateauTimelineEdit,
            slider=self.window.PlateauTimehorizontalSlider,
            calc_constant=UIParameters.PlateauTimeCalcConstant,
            update_model_func=self.update_plateau_time
        )

    def update_plateau_time(self, val):
        self.model.PlateauTime = val