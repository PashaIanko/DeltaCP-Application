from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from sys import exc_info


class SinusPointsNumberCallBackOperator(CallBackOperator):
    def __init__(self, model):
        super().__init__(model)

    def ConnectCallBack(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=SinusUIParameters.PointsNumberSliderMin,
            validator_max=SinusUIParameters.PointsNumberSliderMax,
            validator_accuracy=SinusUIParameters.PointsNumberLineEditAccuracy,
            line_edit=self.window.PointsNumberlineEdit,
            slider_min=SinusUIParameters.PointsNumberSliderMin,
            slider_max=SinusUIParameters.PointsNumberSliderMax,
            slider=self.window.horizontalSliderPointsNumber,
            update_slider_func=self.update_points_number_slider,
            update_line_edit_func=self.update_points_number_line_edit
        )

    def update_points_number_slider(self):
        try:
            self.update_slider(
                line_edit=self.window.PointsNumberlineEdit,
                slider=self.window.horizontalSliderPointsNumber,
                calc_constant=SinusUIParameters.PointsNumberCalcConstant
            )
        except:
            print(exc_info())

    def update_points_number_line_edit(self):
        try:
            self.update_line_edit(
                line_edit=self.window.PointsNumberlineEdit,
                slider=self.window.horizontalSliderPointsNumber,
                calc_constant=SinusUIParameters.PointsNumberCalcConstant,
                update_model_func=self.update_points_number
            )
        except:
            print(exc_info())

    def update_points_number(self, val):
        self.model.PointsNumber = int(val)