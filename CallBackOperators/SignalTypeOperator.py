from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusSignalController import SinusSignalController
from SignalGenerationPackage.UserSignal.UserSignalController import UserSignalController
import sys

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
            try:
                self.SignalController = UserSignalController()
            except:
                print(sys.exc_info())
        # TODO: для меандра и пользовательского сигнала здесь контроллеры добавить
