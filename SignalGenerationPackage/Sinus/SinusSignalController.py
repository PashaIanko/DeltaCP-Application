from SignalGenerationPackage.Sinus.Ui_SinWindow import Ui_SinWindow
from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.Sinus.SinusSignal import SinusSignal
from SignalGenerationPackage.Sinus.SinusObserver import SinusObserver
from SignalGenerationPackage.Sinus.SinusAmplitudeCallBackOperator import SinusAmplitudeCallBackOperator
from SignalGenerationPackage.Sinus.SinusTimeFromCallBackOperator import SinusTimeFromCallBackOperator
from SignalGenerationPackage.Sinus.SinusTimeToCallBackOperator import SinusTimeToCallBackOperator
from SignalGenerationPackage.Sinus.SinusPointsNumberCallBackOperator import SinusPointsNumberCallBackOperator
from SignalGenerationPackage.Sinus.SinusPhaseCallBackOperator import SinusPhaseCallBackOperator
from SignalGenerationPackage.Sinus.SinusOmegaCallBackOperator import SinusOmegaCallBackOperator
import sys

class SinusSignalController(SignalController):

    def __init__(self):
        super().__init__()


    def InitModel(self):
        # creating MVC model
        self.Model = SinusSignal()

    def InitView(self):
        # creating MVC view
        self.View = SinusObserver(self, self.Model)

    # overriden method - here you define personal Graphical Interface
    # (Ui) and show the window
    def InitSignalUI(self):
        self.UserInterface = Ui_SinWindow()

    def InitCallBackOperators(self):
        self.CallbackOperators = \
            [
                SinusAmplitudeCallBackOperator(self.Model),
                SinusTimeFromCallBackOperator(self.Model),
                SinusTimeToCallBackOperator(self.Model),
                SinusPointsNumberCallBackOperator(self.Model),
                SinusPhaseCallBackOperator(self.Model),
                SinusOmegaCallBackOperator(self.Model)
            ]

    # overriden
    def ConnectCallBacks(self):
        for operator in self.CallbackOperators:
            operator.ConnectCallBack(self.UserInterface)
