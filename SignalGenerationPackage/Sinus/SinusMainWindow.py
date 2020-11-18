from PyQt5 import QtWidgets
from PlotCanvas import PlotCanvas
from SignalGenerationPackage.Sinus.Ui_SinusMainWindow import Ui_SinusMainWindow




class SinusMainWindow(QtWidgets.QMainWindow, Ui_SinusMainWindow):
    def __init__(self):
        super().__init__()

        self.SinPlot = PlotCanvas(parent=self)
        self.SinPlot.move(0, 0)
        self.setupUi(self)
