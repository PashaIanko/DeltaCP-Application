from PyQt5 import QtWidgets
from PlotCanvas import PlotCanvas
from SignalGenerationPackage.Sinus.Ui_SinusMainWindow import Ui_SinusMainWindow
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters



class SinusMainWindow(QtWidgets.QMainWindow, Ui_SinusMainWindow):
    def __init__(self):
        super().__init__()

        self.SinPlot = PlotCanvas(parent=self,
                                  width=SinusUIParameters.SinusPlotWidth,
                                  height=SinusUIParameters.SinusPlotHeight)
        self.SinPlot.move(SinusUIParameters.SinusPlotXPosition, SinusUIParameters.SinusPlotYPosition)
        self.setupUi(self)
