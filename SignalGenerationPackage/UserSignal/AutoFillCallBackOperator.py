from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters
from CallBackOperator import CallBackOperator
import pandas as pd
import sys


class AutoFillCallBackOperator(CallBackOperator):
    def __init__(self):
        super().__init__()
        self.configs_path = ".\\SignalGenerationConfigs\\UserSignalConfigs\\SignalConfigs.xlsx"
        self.configs_data = pd.read_excel(self.configs_path)
        self.configs_data.index = self.configs_data['Config Name']

    def ConnectCallBack(self, window):
        self.window = window
        window.AutoFillpushButton.clicked.connect(self.AutoFill)


    def AutoFill(self):
        config_name = self.window.ConfigFileNamelineEdit.text()
        try:
            config_params = self.configs_data.loc[config_name]
            window = self.window
            self.set_signal_parameters(
                [
                    [config_params['Start Time'],           UserSignalUIParameters.StartTimeCalcConstant,           window.StartTimehorizontalSlider],
                    [config_params['Acceleration Time'],    UserSignalUIParameters.AccelerationTimeCalcConstant,    window.AccelerationTimehorizontalSlider],
                    [config_params['Plateau Time'],         UserSignalUIParameters.PlateauTimeCalcConstant,         window.PlateauTimehorizontalSlider],
                    [config_params['Deceleration Time'],    UserSignalUIParameters.DecelerationTimeCalcConstant,    window.DecelerationTimehorizontalSlider],
                    [config_params['Low Level Frequency'],  UserSignalUIParameters.LowLevelFrequencyCalcConstant,   window.LowLevelFrequencyhorizontalSlider],
                    [config_params['High Level Frequency'], UserSignalUIParameters.HighLevelFrequencyCalcConstant,  window.HighLevelFrequencyhorizontalSlider],
                    [config_params['Vertical Offset'],      UserSignalUIParameters.VerticalOffsetCalcConstant,      window.VerticalOffsethorizontalSlider],
                    [config_params['Points Number'],        UserSignalUIParameters.PointsNumberCalcConstant,        window.PointsNumberhorizontalSlider],
                    [config_params['End Time'],             UserSignalUIParameters.EndTimeCalcConstant,             window.EndTimehorizontalSlider]
                ]
            )
        except:
            print(sys.exc_info())


    # def all_widgets_are_ready(self, values_and_widgets):
    #     for v in values_and_widgets:
    #         value_to_set = v[0]
    #         constant = v[1]
    #         slider = v[2]
    #
    #         if slider.value() != value_to_set:
    #             return False
    #     return True


    def set_signal_parameters(self, value_widgets):
        # TODO: Не может за один цикл синхронизировать слайдеры и текстовые поля, Не знаю что за баг
        for v in value_widgets:
            value_to_set = v[0]
            constant = v[1]
            slider = v[2]
            slider.setValue(value_to_set * constant)


            


