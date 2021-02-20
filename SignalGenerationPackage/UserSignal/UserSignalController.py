from SignalGenerationPackage.SignalController import  SignalController
from SignalGenerationPackage.UserSignal.UserSignal import UserSignal
from SignalGenerationPackage.UserSignal.UserSignalObserver import UserSignalObserver
from SignalGenerationPackage.UserSignal.AccelerationTimeCallBackOperator import AccelerationTimeCallBackOperator
from SignalGenerationPackage.UserSignal.DecelerationTimeCallBackOperator import DecelerationTimeCallBackOperator
from SignalGenerationPackage.UserSignal.HighLevelFrequencyCallBackOperator import HighLevelFrequencyCallBackOperator
from SignalGenerationPackage.UserSignal.LowLevelFrequencyCallBackOperator import LowLevelFrequencyCallBackOperator
from SignalGenerationPackage.UserSignal.PlateauTimeCallBackOperator import PlateauTimeCallBackOperator
from SignalGenerationPackage.UserSignal.PointsNumberCallBackOperator import PointsNumberCallBackOperator
from SignalGenerationPackage.UserSignal.EndTimeCallBackOperator import EndTimeCallBackOperator
from SignalGenerationPackage.UserSignal.StartTimeCallBackOperator import StartTimeCallBackOperator
from SignalGenerationPackage.UserSignal.VerticalOffsetCallBackOperator import VerticalOffsetCallBackOperator
from SignalGenerationPackage.UserSignal.AutoFillCallBackOperator import AutoFillCallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalMainWindow import UserSignalMainWindow
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters
from CallBackOperators.ForwardSendingOperator import ForwardSendingOperator


class UserSignalController(SignalController):

    def __init__(self):
        super().__init__()

    # overridden
    def init_model(self):
        self.model = UserSignal()

    # overridden
    def init_observer(self):
        self.observer = UserSignalObserver(self.model, self.main_window.plot)

    # overridden
    def init_main_window(self):
        self.main_window = UserSignalMainWindow()

    # overridden
    def init_param_names(self):
        self.param_names = [
            'Start Time', 'Acceleration Time', 'Plateau Time',
            'Deceleration Time', 'Low Level Frequency', 'High Level Frequency',
            'Vertical Offset', 'Points Number', 'End Time'
        ]

    # overridden
    def init_slider_constants(self):
        self.slider_constants = [
            UserSignalUIParameters.StartTimeCalcConstant,
            UserSignalUIParameters.AccelerationTimeCalcConstant,
            UserSignalUIParameters.PlateauTimeCalcConstant,
            UserSignalUIParameters.DecelerationTimeCalcConstant,
            UserSignalUIParameters.LowLevelFrequencyCalcConstant,
            UserSignalUIParameters.HighLevelFrequencyCalcConstant,
            UserSignalUIParameters.VerticalOffsetCalcConstant,
            UserSignalUIParameters.PointsNumberCalcConstant,
            UserSignalUIParameters.EndTimeCalcConstant
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
            ui.VerticalOffsethorizontalSlider,
            ui.PointsNumberhorizontalSlider,
            ui.EndTimehorizontalSlider,
        ]

    def init_plot_widget(self):
        self.plot_widget = self.main_window.user_interface.plot_widget

    def init_callback_operators(self):
        self.callback_operators = \
            [
                StartTimeCallBackOperator(self.model),
                AccelerationTimeCallBackOperator(self.model),
                PlateauTimeCallBackOperator(self.model),
                DecelerationTimeCallBackOperator(self.model),
                EndTimeCallBackOperator(self.model),
                VerticalOffsetCallBackOperator(self.model),
                HighLevelFrequencyCallBackOperator(self.model),
                LowLevelFrequencyCallBackOperator(self.model),
                PointsNumberCallBackOperator(self.model),
                AutoFillCallBackOperator(self.slider_constants, self.param_names, self.sliders, model=None)
            ]

    # overridden
    def append_sending_operator(self):
        self.callback_operators.append(ForwardSendingOperator(self.main_window, self.plot_widget, DebugMode=True))
        # Подключится к виджетам окна с генерацией сигнала.
        # Чтобы отправить сигнал можно было прямо из окна генерирования сигнала (удобство польз-ля)
