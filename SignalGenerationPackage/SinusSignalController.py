from PyQt5 import QtWidgets
from SignalGenerationPackage.SignalController import SignalController

class SinusSignalController():#(SignalController):

    def __init__(self):
        super().__init__()
        self.InitSignalUI()

    def InitSignalUI(self):
        self.button = QtWidgets.QPushButton("Ok", self)
        self.button.move(200, 200)
        self.button.clicked.connect(self.continue2)
        self.setGeometry(600, 200, 500, 300)
        self.show()


    def continue2(self):
        print('callback')