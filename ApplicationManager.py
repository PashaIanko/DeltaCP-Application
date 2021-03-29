from PyQt5 import QtWidgets
from Graphics import Ui_MainWindow
from ConnectionPackage.ConnectionModule import ConnectionModule
from SignalGenerationPackage.SignalGenerationModule import SignalGenerationModule
from FrequencySettingPackage.FrequencySettingModule import FrequencySettingModule
from LogVisualizationPackage.LogVisualizationModule import LogVisualizationModule



class ApplicationManager:

    def __init__(self):

        self.ApplicationModules = \
            [
                ConnectionModule(),
                FrequencySettingModule(),
                SignalGenerationModule(),
                LogVisualizationModule()
            ]

        self.MainWindow = QtWidgets.QMainWindow()
        self.UserInterface = Ui_MainWindow()
        self.UserInterface.setupUi(self.MainWindow)
        self.RunAllModules()

    def RunAllModules(self):
        for module in self.ApplicationModules:
            module.Run(self.UserInterface)


