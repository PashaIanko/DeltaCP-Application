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

class SinusSignalController(SignalController):

    def __init__(self):
        super().__init__()


    def init_model(self):
        self.model = SinusSignal()

    def init_observer(self):
        self.observer = SinusObserver(self.model, self.main_window.SinPlot)

    def init_main_window(self):
        self.main_window = SinusMainWindow()

    def init_callback_operators(self):
        self.callback_operators = \
            [
                SinusAmplitudeCallBackOperator(self.model),
                SinusTimeFromCallBackOperator(self.model),
                SinusTimeToCallBackOperator(self.model),
                SinusPointsNumberCallBackOperator(self.model),
                SinusPhaseCallBackOperator(self.model),
                SinusOmegaCallBackOperator(self.model)
            ]
