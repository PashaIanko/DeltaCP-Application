from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusSignalController import SinusSignalController
from SignalGenerationPackage.UserSignal.UserSignalController import UserSignalController
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignalController import DynamicPointsDensitySignalController
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
            try:
                self.SignalController = SinusSignalController()
            except:
                print(sys.exc_info())
        elif signal_text == 'user signal':
            self.SignalController = UserSignalController()
        elif signal_text == 'dynamic points density':
            try:
                self.SignalController = DynamicPointsDensitySignalController()
            except:
                print(sys.exc_info())
        # TODO: для меандра и пользовательского сигнала здесь контроллеры добавить
        # TODO: убрать ветвление, вставить словарь
