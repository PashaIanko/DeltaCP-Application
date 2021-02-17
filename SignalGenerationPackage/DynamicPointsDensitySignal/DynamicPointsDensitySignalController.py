from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignal import DynamicPointsDensitySignal
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignalObserver import DynamicPointsDensitySignalObserver
from SignalGenerationPackage.DynamicPointsDensitySignal.AccelerationTimeCallBackOperator import AccelerationTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DecelerationTimeCallBackOperator import DecelerationTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.HighLevelFrequencyCallBackOperator import HighLevelFrequencyCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.LowLevelFrequencyCallBackOperator import LowLevelFrequencyCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.PlateauTimeCallBackOperator import PlateauTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.PointsDensityCallBackOperator import PointsDensityCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.EndTimeCallBackOperator import EndTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.StartTimeCallBackOperator import StartTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.AutoFillCallBackOperator import AutoFillCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityMainWindow import DynamicPointsDensityMainWindow
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters
from CallBackOperators.ForwardSendingOperator import ForwardSendingOperator


class DynamicPointsDensitySignalController(SignalController):

    def __init__(self):
        super().__init__()

    # overridden
    def init_model(self):
        self.model = DynamicPointsDensitySignal()

    # overridden
    def init_observer(self):
        self.observer = DynamicPointsDensitySignalObserver(self.model, self.main_window.plot)
        # TODO: Посмотри, этот метод везде одинаков, можно в родителя

    # overridden
    def init_main_window(self):
        self.main_window = DynamicPointsDensityMainWindow()

    # overridden
    def init_callback_operators(self):
        import sys
        try:
            self.callback_operators = \
                [
                    StartTimeCallBackOperator(self.model),
                    AccelerationTimeCallBackOperator(self.model),
                    PlateauTimeCallBackOperator(self.model),
                    DecelerationTimeCallBackOperator(self.model),
                    EndTimeCallBackOperator(self.model),
                    HighLevelFrequencyCallBackOperator(self.model),
                    LowLevelFrequencyCallBackOperator(self.model),
                    PointsDensityCallBackOperator(self.model),
                    AutoFillCallBackOperator(self.slider_constants, self.param_names, self.sliders, model=None),

                ]
        except:
            print(sys.exc_info())


    # overridden
    def append_sending_operator(self):
        self.callback_operators.append(ForwardSendingOperator(DebugMode=True))
        # Подключится к виджетам окна с генерацией сигнала.
        # Чтобы отправить сигнал можно было прямо из окна генерирования сигнала (удобство польз-ля)

    # overridden
    def init_param_names(self):
        self.param_names = [
            'Start Time', 'Acceleration Time', 'Plateau Time', 'Deceleration Time', 'Low Level Frequency',
            'High Level Frequency', 'Points Density', 'End Time']

    # overridden
    def init_slider_constants(self):
        self.slider_constants = [
            DynamicPointsDensityUIParameters.StartTimeCalcConstant,
            DynamicPointsDensityUIParameters.AccelerationTimeCalcConstant,
            DynamicPointsDensityUIParameters.PlateauTimeCalcConstant,
            DynamicPointsDensityUIParameters.DecelerationTimeCalcConstant,
            DynamicPointsDensityUIParameters.LowLevelFrequencyCalcConstant,
            DynamicPointsDensityUIParameters.HighLevelFrequencyCalcConstant,
            DynamicPointsDensityUIParameters.PointsDensityCalcConstant,
            DynamicPointsDensityUIParameters.EndTimeCalcConstant,
        ]

    # overridden
    def init_sliders(self):
        ui = self.main_window.user_interface
        self.sliders = [
            ui.StartTimehorizontalSlider,
            ui.AccelerationTimehorizontalSlider,
            ui.PlateauTimehorizontalSlider,
            ui.DecelerationTimehorizontalSlider,
            ui.LowLevelFrequencyhorizontalSlider,
            ui.HighLevelFrequencyhorizontalSlider,
            ui.PointsDensityhorizontalSlider,
            ui.EndTimehorizontalSlider
        ]