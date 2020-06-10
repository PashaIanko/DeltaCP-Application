from SignalGenerationPackage.Sinus.Ui_SinWindow import Ui_SinWindow
from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.Sinus.SinusSignal import SinusSignal
from SignalGenerationPackage.Sinus.SinusObserver import SinusObserver
import sys

class SinusSignalController(SignalController):

    def __init__(self):
        super().__init__()

        # creating MVC model
        self.Model = SinusSignal()

        # creating MVC view
        self.View = SinusObserver(self, self.Model)



    # overriden method - here you define personal Graphical Interface
    # (Ui) and show the window
    def InitSignalUI(self):
        self.ui = Ui_SinWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ConnectCallBacks()

    def ConnectCallBacks(self):
        self.ui.TestpushButton1.clicked.connect(self.SetAmplitude)

    def SetAmplitude(self):
        print('in callbackk')
        self.Model.amplitude = 1
