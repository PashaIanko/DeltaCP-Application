from CallBackOperator import CallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters

class VerticalOffsetCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model


    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=DynamicPointsDensityUIParameters.VerticalOffsetSliderMin,
            validator_max=DynamicPointsDensityUIParameters.VerticalOffsetSliderMax,
            validator_accuracy=DynamicPointsDensityUIParameters.VerticalOffsetLineEditAccuracy,
            line_edit=window.VerticalOffsetlineEdit,
            slider_min=DynamicPointsDensityUIParameters.VerticalOffsetSliderMin,
            slider_max=DynamicPointsDensityUIParameters.VerticalOffsetSliderMax,
            slider=window.VerticalOffsethorizontalSlider,
            update_slider_func=self.update_vertical_offset_slider,
            update_line_edit_func=self.update_vertical_offset_line_edit
        )

    def update_vertical_offset_slider(self):
        self.update_slider(
            line_edit=self.window.VerticalOffsetlineEdit,
            slider=self.window.VerticalOffsethorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.VerticalOffsetCalcConstant
        )

    def update_vertical_offset_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.VerticalOffsetlineEdit,
            slider=self.window.VerticalOffsethorizontalSlider,
            calc_constant=DynamicPointsDensityUIParameters.VerticalOffsetCalcConstant,
            update_model_func=self.update_vertical_offset
        )

    def update_vertical_offset(self, val):
        self.Model.VerticalOffset = val