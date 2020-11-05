from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters

class VerticalOffsetCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model


    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.VerticalOffsetSliderMin,
            validator_max=UserSignalUIParameters.VerticalOffsetSliderMax,
            validator_accuracy=UserSignalUIParameters.VerticalOffsetLineEditAccuracy,
            line_edit=window.VerticalOffsetlineEdit,
            slider_min=UserSignalUIParameters.VerticalOffsetSliderMin,
            slider_max=UserSignalUIParameters.VerticalOffsetSliderMax,
            slider=window.VerticalOffsethorizontalSlider,
            update_slider_func=self.update_vertical_offset_slider,
            update_line_edit_func=self.update_vertical_offset_line_edit
        )

    def update_vertical_offset_slider(self):
        self.update_slider(
            line_edit=self.window.VerticalOffsetlineEdit,
            slider=self.window.VerticalOffsethorizontalSlider,
            calc_constant=UserSignalUIParameters.VerticalOffsetCalcConstant
        )

    def update_vertical_offset_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.VerticalOffsetlineEdit,
            slider=self.window.VerticalOffsethorizontalSlider,
            calc_constant=UserSignalUIParameters.VerticalOffsetCalcConstant,
            update_model_func=self.update_vertical_offset
        )

    def update_vertical_offset(self, val):
        print(f'updating model, now val = {val}')
        self.Model.VerticalOffset = val