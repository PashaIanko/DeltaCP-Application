from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.Sinus.SinusSignal import SinusSignal
from SignalGenerationPackage.Sinus.SinusObserver import SinusObserver
from SignalGenerationPackage.Sinus.SinusAmplitudeCallBackOperator import SinusAmplitudeCallBackOperator
from SignalGenerationPackage.Sinus.SinusTimeFromCallBackOperator import SinusTimeFromCallBackOperator
from SignalGenerationPackage.Sinus.SinusTimeToCallBackOperator import SinusTimeToCallBackOperator
from SignalGenerationPackage.Sinus.SinusPointsNumberCallBackOperator import SinusPointsNumberCallBackOperator
from SignalGenerationPackage.Sinus.SinusPhaseCallBackOperator import SinusPhaseCallBackOperator
from SignalGenerationPackage.Sinus.SinusOmegaCallBackOperator import SinusOmegaCallBackOperator
from SignalGenerationPackage.Sinus.SinusMainWindow import SinusMainWindow
from CallBackOperators.ForwardSendingOperator import ForwardSendingOperator
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from SignalGenerationPackage.Sinus.AutoFillCallBackOperator import AutoFillCallBackOperator

class SinusSignalController(SignalController):

    def __init__(self):
        super().__init__()

    # overridden
    def init_model(self):
        self.model = SinusSignal()

    # overridden
    def init_observer(self):
        self.observer = SinusObserver(self.model, self.main_window.plot)

    # overridden
    def init_main_window(self):
        self.main_window = SinusMainWindow()

    # overridden
    def init_callback_operators(self):
        self.callback_operators = \
            [
                SinusAmplitudeCallBackOperator(self.model),
                SinusTimeFromCallBackOperator(self.model),
                SinusTimeToCallBackOperator(self.model),
                SinusPointsNumberCallBackOperator(self.model),
                SinusPhaseCallBackOperator(self.model),
                SinusOmegaCallBackOperator(self.model),
                AutoFillCallBackOperator(self.slider_constants, self.param_names, self.sliders, model=None),
            ]

    # overridden
    def init_plot_widget(self):
        self.plot_widget = self.main_window.user_interface.frame

    # overridden
    def append_sending_operator(self):
        self.callback_operators.append(ForwardSendingOperator(self.main_window, self.plot_widget, DebugMode=True))

    # overridden
    def init_param_names(self):
        self.param_names = [
            "Phase", "Omega", "Points Number", "Time From", "Time To", "Amplitude"
        ]

    # overridden
    def init_slider_constants(self):
        self.slider_constants = [
            SinusUIParameters.PhaseCalcConstant,
            SinusUIParameters.OmegaCalcConstant,
            SinusUIParameters.PointsNumberCalcConstant,
            SinusUIParameters.TimeFromCalcConstant,
            SinusUIParameters.TimeToCalcConstant,
            SinusUIParameters.AmplitudeCalcConstant
        ]

    def init_sliders(self):
        ui = self.main_window.user_interface
        self.sliders = [
            ui.horizontalSliderPhase,
            ui.horizontalSliderOmega,
            ui.horizontalSliderPointsNumber,
            ui.horizontalSliderTimeFrom,
            ui.horizontalSliderTimeTo,
            ui.horizontalSliderAmplitude
        ]