from PyQt5 import QtWidgets
from Graphics import Ui_MainWindow
from ConnectionPackage.ConnectionModule import ConnectionModule

class ApplicationManager(QtWidgets.QMainWindow):

    ApplicationModules = \
        [
        ConnectionModule()
        #SignalGenerationModule()
        ]

    def __init__(self):
        super(ApplicationManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.RunAllModules()

    def RunAllModules(self):
        for module in self.ApplicationModules:
            module.Run(self.ui)
