from PyQt5 import QtWidgets
from PlotCanvas import PlotCanvas
from SignalSendingPackage.Ui_VisualizerMainWindow import Ui_VisualizerMainWindow


class VisualizerMainWindow(QtWidgets.QMainWindow, Ui_VisualizerMainWindow):
    def __init__(self):
        super().__init__()

        self.VisualizerPlot = PlotCanvas(parent=self)
        self.VisualizerPlot.move(0, 30) # (SinusUIParameters.SinusPlotXPosition, SinusUIParameters.SinusPlotYPosition)
        self.setupUi(self)
