
from CallBackOperator import CallBackOperator
from PyQt5 import QtWidgets
from SignalGenerationPackage.SinusSignalController import SinusSignalController


class SignalTypeOperator(CallBackOperator):
    def __init__(self):
        self.UserInterface = None


    def ConnectCallBack(self, UserInterface):
        UserInterface.SignalTypecomboBox.currentIndexChanged.connect(self.SetSignalType)
        self.UserInterface = UserInterface

    def SetSignalType(self):
        print('in callback')
        self.SignalController = SinusSignalController()
