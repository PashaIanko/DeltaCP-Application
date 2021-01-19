from PyQt5 import QtWidgets
from Graphics import Ui_MainWindow
from ConnectionPackage.ConnectionModule import ConnectionModule
from SignalGenerationPackage.SignalGenerationModule import SignalGenerationModule
from SignalSendingPackage.SignalSendingModule import SignalSendingModule
from FrequencySettingPackage.FrequencySettingModule import FrequencySettingModule
from AccelerDecelerTimePackage.AccelerDecelerTimeModule import AccelerDecelerTimeModule


class ApplicationManager(QtWidgets.QMainWindow):

    def __init__(self):

        self.ApplicationModules = \
            [
                ConnectionModule(),
                FrequencySettingModule(),
                AccelerDecelerTimeModule(),
                SignalGenerationModule(),
                SignalSendingModule()
            ]

        super(ApplicationManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.RunAllModules()

    def RunAllModules(self):
        for module in self.ApplicationModules:
            module.Run(self)
