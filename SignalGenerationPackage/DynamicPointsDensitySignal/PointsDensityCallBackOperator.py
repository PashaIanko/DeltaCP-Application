from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters

class PointsDensityCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model


    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.PointsDensitySliderMin,
            validator_max=UserSignalUIParameters.PointsDensitySliderMax,
            validator_accuracy=UserSignalUIParameters.PointsDensityLineEditAccuracy,
            line_edit=window.PointsDensitylineEdit,
            slider_min=UserSignalUIParameters.PointsDensitySliderMin,
            slider_max=UserSignalUIParameters.PointsDensitySliderMax,
            slider=window.PointsDensityhorizontalSlider,
            update_slider_func=self.update_points_density_slider,
            update_line_edit_func=self.update_points_density_line_edit
        )

    def update_points_density_slider(self):
        self.update_slider(
            line_edit=self.window.PointsDensitylineEdit,
            slider=self.window.PointsDensityhorizontalSlider,
            calc_constant=UserSignalUIParameters.PointsDensityCalcConstant
        )

    def update_points_density_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.PointsDensitylineEdit,
            slider=self.window.PointsDensityhorizontalSlider,
            calc_constant=UserSignalUIParameters.PointsDensityCalcConstant,
            update_model_func=self.update_vertical_offset
        )

    def update_vertical_offset(self, val):
        self.Model.PointsDensity = val