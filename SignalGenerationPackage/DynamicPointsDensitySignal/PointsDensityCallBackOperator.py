from CallBackOperator import CallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters

class PointsDensityCallBackOperator(CallBackOperator):

    def __init__(self, model):
        super().__init__(model)

    # overridden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=DynamicPointsDensityUIParameters.PointsDensitySliderMin,
            validator_max=DynamicPointsDensityUIParameters.PointsDensitySliderMax,
            validator_accuracy=DynamicPointsDensityUIParameters.PointsDensityLineEditAccuracy,
            line_edit=window.PointsDensitylineEdit,
            slider_min=DynamicPointsDensityUIParameters.PointsDensitySliderMin,
            slider_max=DynamicPointsDensityUIParameters.PointsDensitySliderMax,
            slider=window.PointsDensityhorizontalSlider,
            update_slider_func=self.update_points_density_slider,
            update_line_edit_func=self.update_points_density_line_edit
        )

    def update_points_density_slider(self):
        self.update_slider(
            line_edit=self.window.PointsDensitylineEdit,
            slider=self.window.PointsDensityhorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.PointsDensityCalcConstant
        )

    def update_points_density_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.PointsDensitylineEdit,
            slider=self.window.PointsDensityhorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.PointsDensityCalcConstant,
            update_model_func=self.update_vertical_offset
        )

    def update_vertical_offset(self, val):
        self.model.PointsDensity = val