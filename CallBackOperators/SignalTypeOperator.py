
from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusSignalController import SinusSignalController


class SignalTypeOperator(CallBackOperator):
    def __init__(self):
        self.UserInterface = None



    def ConnectCallBack(self, UserInterface):
        UserInterface.SignalTypecomboBox.currentIndexChanged.connect(self.StartSignalGeneration)
        self.UserInterface = UserInterface

    def StartSignalGeneration(self):
        if self.UserInterface.SignalTypecomboBox.currentText() == 'sin':
            self.SignalController = SinusSignalController()
