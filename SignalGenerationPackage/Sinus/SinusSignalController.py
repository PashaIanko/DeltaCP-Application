from SignalGenerationPackage.Sinus.Ui_SinWindow import Ui_SinWindow
from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.Sinus.SinusSignal import SinusSignal



class SinusSignalController(SignalController):

    def __init__(self):
        super().__init__()

        # creating MVC model
        self.Signal = SinusSignal()



    # overriden method - here you define personal Graphical Interface (Ui) and show the window
    def InitSignalUI(self):
        self.ui = Ui_SinWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.ui.TestpushButton1.clicked.connect(self.TestCallback)

    def TestCallback(self):
        print('in callbackk')
