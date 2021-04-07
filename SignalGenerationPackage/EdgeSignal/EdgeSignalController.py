from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.EdgeSignal.EdgeSignal import EdgeSignal
from SignalGenerationPackage.EdgeSignal.EdgeSignalObserver import EdgeSignalObserver
from SignalGenerationPackage.EdgeSignal.EdgeSignalMainWindow import EdgeSignalMainWindow
from SignalGenerationPackage.EdgeSignal.EdgeSignalUIParameters import EdgeSignalUIParameters
from CallBackOperators.PIDSendingOperator import PIDSendingOperator

from SignalGenerationPackage.EdgeSignal.CallBacks.AccelerationTimeCallBackOperator import AccelerationTimeCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.DecelerationTimeCallBackOperator import DecelerationTimeCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.HighLevelFrequencyCallBackOperator import HighLevelFrequencyCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.LowLevelFrequencyCallBackOperator import LowLevelFrequencyCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.PlateauTimeCallBackOperator import PlateauTimeCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.EndTimeCallBackOperator import EndTimeCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.StartTimeCallBackOperator import StartTimeCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.AutoFillCallBackOperator import AutoFillCallBackOperator
from SignalGenerationPackage.EdgeSignal.CallBacks.RequestFrequencyCallBackOperator import RequestFrequencyCallBackOperator

from Ranges import EdgeSignalRanges


class EdgeSignalController(SignalController):

    def __init__(self):
        super().__init__()

    # overridden
    def init_model(self):
        self.model = EdgeSignal()

    # overridden
    def init_observer(self):
        self.observer = EdgeSignalObserver(self.model, self.main_window.plot)

    # overridden
    def init_main_window(self):
        self.main_window = EdgeSignalMainWindow()

    # overridden
    def init_param_names(self):
        self.param_names = [
            'Start Time', 'Acceleration Time', 'Plateau Time',
            'Deceleration Time', 'Low Level Frequency', 'High Level Frequency',
            'End Time', 'Request Frequency'  # TODO: в таком же месте для UserSignal убрать Vertical Offset
        ]

    # overridden
    def init_slider_constants(self):
        self.slider_constants = [
            EdgeSignalUIParameters.StartTimeCalcConstant,
            EdgeSignalUIParameters.AccelerationTimeCalcConstant,
            EdgeSignalUIParameters.PlateauTimeCalcConstant,
            EdgeSignalUIParameters.DecelerationTimeCalcConstant,
            EdgeSignalUIParameters.LowLevelFrequencyCalcConstant,
            EdgeSignalUIParameters.HighLevelFrequencyCalcConstant,
            EdgeSignalUIParameters.EndTimeCalcConstant,
            EdgeSignalUIParameters.RequestFreqCalcConstant
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
            ui.EndTimehorizontalSlider,
            ui.RequestFrequencyhorizontalSlider
        ]

    def init_plot_widget(self):
        self.plot_widget = self.main_window.user_interface.plot_widget

    def init_callback_operators(self):
        self.callback_operators = \
            [
                StartTimeCallBackOperator       (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_start_range),
                AccelerationTimeCallBackOperator(self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_acceleration_range),
                PlateauTimeCallBackOperator     (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_plateau_range),
                DecelerationTimeCallBackOperator(self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_deceleration_range),
                EndTimeCallBackOperator(self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_end_range),
                HighLevelFrequencyCallBackOperator(self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.high_freq_range),
                LowLevelFrequencyCallBackOperator(self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.low_freq_range),
                RequestFrequencyCallBackOperator(self.main_window.user_interface, self.model),
                #AutoFillCallBackOperator(self.slider_constants, self.param_names, self.sliders, model=None)
            ]

    # overridden
    def append_sending_operator(self):
        self.callback_operators.append(PIDSendingOperator(self.main_window, self.plot_widget, model=self.model, DebugMode=False, SendRetry=True))
        # Подключится к виджетам окна с генерацией сигнала.
        # Чтобы отправить сигнал можно было прямо из окна генерирования сигнала (удобство польз-ля)
