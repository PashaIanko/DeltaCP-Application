from CallBackOperator import CallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters

class PointsNumberCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=UserSignalUIParameters.PointsNumberSliderMin,
            validator_max=UserSignalUIParameters.PointsNumberSliderMax,
            validator_accuracy=UserSignalUIParameters.PointsNumberLineEditAccuracy,
            line_edit=window.PointsNumberlineEdit,
            slider_min=UserSignalUIParameters.PointsNumberSliderMin,
            slider_max=UserSignalUIParameters.PointsNumberSliderMax,
            slider=window.PointsNumberhorizontalSlider,
            update_slider_func=self.update_points_number_slider,
            update_line_edit_func=self.update_points_number_line_edit
        )

    def update_points_number_slider(self):
        try:
            self.update_slider(
                line_edit=self.window.PointsNumberlineEdit,
                slider=self.window.PointsNumberhorizontalSlider,
                calc_constant=UserSignalUIParameters.PointsNumberCalcConstant
            )
        except:
            import sys
            print(sys.exc_info())

    def update_points_number_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.PointsNumberlineEdit,
                slider=self.window.PointsNumberhorizontalSlider,
                calc_constant=UserSignalUIParameters.PointsNumberCalcConstant,
                update_model_func=self.update_points_number
            )
        except:
            import sys
            print(sys.exc_info())

    def update_points_number(self, val):
        print(f'updating model, now val = {val}')
        self.Model.PointsNumber = int(val)