from PyQt5 import QtWidgets
from PlotCanvas import PlotCanvas
from SignalSendingPackage.Ui_VisualizerMainWindow import Ui_VisualizerMainWindow
from LoggersConfig import loggers


class VisualizerMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_is_closed = False
        #self.VisualizerPlot = PlotCanvas(parent=self, width=8, height=7)
        #self.VisualizerPlot.move(20, 29) # TODO: Вывести константы в отдельный класс
        self.VisualizerPlot = None
        self.user_interface = Ui_VisualizerMainWindow()
        self.setup_ui()
        self.setup_plot()

    def closeEvent(self, event):
        loggers['Debug'].debug(f'VisualizerMainWindow: closeEvent: signal sending visualization window was closed')
        loggers['Application'].info(
            f'VisualizerMainWindow: closeEvent: signal sending visualization window was closed'
        )
        self.window_is_closed = True

    def setup_plot(self):
        self.VisualizerPlot = self.user_interface.frame

    def setup_ui(self):
        self.user_interface.setupUi(self)
