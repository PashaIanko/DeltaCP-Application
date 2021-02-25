from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusSignalController import SinusSignalController
from SignalGenerationPackage.UserSignal.UserSignalController import UserSignalController
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignalController import DynamicPointsDensitySignalController
from SignalGenerationPackage.EdgeSignal.EdgeSignalController import EdgeSignalController

class SignalTypeOperator(CallBackOperator):
    def __init__(self):
        self.UserInterface = None



    def ConnectCallBack(self, UserInterface):
        UserInterface.SignalTypecomboBox.currentIndexChanged.connect(self.StartSignalGeneration)
        self.UserInterface = UserInterface

    def StartSignalGeneration(self):
        signal_text = self.UserInterface.SignalTypecomboBox.currentText()
        if signal_text == 'sin':
            self.SignalController = SinusSignalController()
        elif signal_text == 'user signal':
            self.SignalController = UserSignalController()
        elif signal_text == 'dynamic points density':
            self.SignalController = DynamicPointsDensitySignalController()
        elif signal_text == 'edge signal':
            self.SignalController = EdgeSignalController()
        # TODO: убрать ветвление, вставить словарь
