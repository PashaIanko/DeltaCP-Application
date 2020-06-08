from CallBackOperator import CallBackOperator
from SignalGenerationPackage.SinusSignalController import SinusSignalController
from PyQt5 import QtWidgets

class Test():#(SignalController):

    def __init__(self):
        #super().__init__()
        self.InitSignalUI()

    def InitSignalUI(self):
        self.button = QtWidgets.QPushButton("Ok", self)
        self.button.move(200, 200)
        self.button.clicked.connect(self.continue2)
        self.setGeometry(600, 200, 500, 300)
        self.show()


    def continue2(self):
        print('callback')

class SignalTypeOperator(CallBackOperator):
    def __init__(self):
        self.UserInterface = None
        self.MainWindow = None
        self.SignalController = None

    def SetMainWindow(self, MainWindow):
        self.MainWindow = MainWindow

    def ConnectCallBack(self, UserInterface):
        UserInterface.SignalTypecomboBox.currentIndexChanged.connect(self.SetSignalType)
        self.UserInterface = UserInterface

    def SetSignalType(self):
        print('in callback')
        arg = self.UserInterface.SignalTypecomboBox.currentText()
        if(arg == 'sin'):
            self.SignalController = Test()  # SinusSignalController()






