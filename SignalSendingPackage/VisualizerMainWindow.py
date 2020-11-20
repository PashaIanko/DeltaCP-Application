from PyQt5 import QtWidgets
from PlotCanvas import PlotCanvas
from SignalSendingPackage.Ui_VisualizerMainWindow import Ui_VisualizerMainWindow


class VisualizerMainWindow(QtWidgets.QMainWindow, Ui_VisualizerMainWindow):
    def __init__(self):
        super().__init__()

        self.VisualizerPlot = PlotCanvas(parent=self, width=8, height=7)
        self.VisualizerPlot.move(20, 29) # TODO: Вывести константы в отдельный класс
        self.setupUi(self)
