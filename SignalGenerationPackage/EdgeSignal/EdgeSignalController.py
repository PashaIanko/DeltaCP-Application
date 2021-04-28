from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.EdgeSignal.EdgeSignal import EdgeSignal
from SignalGenerationPackage.EdgeSignal.EdgeSignalObserver import EdgeSignalObserver
from SignalGenerationPackage.EdgeSignal.EdgeSignalMainWindow import EdgeSignalMainWindow
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
from SignalGenerationPackage.SliderTextPair import SliderTextPair
from DebugConfigs import DebugConfigs


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
            'End Time', 'Request Frequency'
        ]

    # overridden
    def init_slider_text_pairs(self):
        ui = self.main_window.user_interface
        self.slider_text_pairs = [
            SliderTextPair(ui.StartTimehorizontalSlider, ui.StartTimelineEdit, EdgeSignalRanges.t_start_range.calc_constant),
            SliderTextPair(ui.AccelerationTimehorizontalSlider, ui.AccelerationTimelineEdit, EdgeSignalRanges.t_acceleration_range.calc_constant),
            SliderTextPair(ui.PlateauTimehorizontalSlider, ui.PlateauTimelineEdit, EdgeSignalRanges.t_plateau_range.calc_constant),
            SliderTextPair(ui.DecelerationTimehorizontalSlider, ui.DecelerationTimelineEdit, EdgeSignalRanges.t_deceleration_range.calc_constant),
            SliderTextPair(ui.LowLevelFrequencyhorizontalSlider, ui.LowLevelFrequencylineEdit, EdgeSignalRanges.low_freq_range.calc_constant),
            SliderTextPair(ui.HighLevelFrequencyhorizontalSlider, ui.HighLevelFrequencylineEdit, EdgeSignalRanges.high_freq_range.calc_constant),
            SliderTextPair(ui.EndTimehorizontalSlider, ui.EndTimelineEdit, EdgeSignalRanges.t_end_range.calc_constant),
            SliderTextPair(ui.RequestFrequencyhorizontalSlider, ui.RequestFrequencylineEdit, EdgeSignalRanges.request_freq_range.calc_constant)
        ]

    # overridden
    def init_plot_widget(self):
        self.plot_widget = self.main_window.user_interface.plot_widget

    # overridden
    def init_callback_operators(self):
        self.callback_operators = \
            [
                StartTimeCallBackOperator           (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_start_range),
                AccelerationTimeCallBackOperator    (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_acceleration_range),
                PlateauTimeCallBackOperator         (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_plateau_range),
                DecelerationTimeCallBackOperator    (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_deceleration_range),
                EndTimeCallBackOperator             (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.t_end_range),
                HighLevelFrequencyCallBackOperator  (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.high_freq_range),
                LowLevelFrequencyCallBackOperator   (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.low_freq_range),
                RequestFrequencyCallBackOperator    (self.main_window.user_interface, self.model, value_range=EdgeSignalRanges.request_freq_range),
                AutoFillCallBackOperator            (self.main_window.user_interface, self.param_names, self.slider_text_pairs, model=None)
            ]

    # overridden
    def append_sending_operator(self):
        self.callback_operators.append(PIDSendingOperator(self.main_window, self.plot_widget, model=self.model,
                                                          DebugMode=DebugConfigs.PIDOperatorDebug, SendRetry=True))
        # Подключится к виджетам окна с генерацией сигнала.
        # Чтобы отправить сигнал можно было прямо из окна генерирования сигнала (удобство польз-ля)
