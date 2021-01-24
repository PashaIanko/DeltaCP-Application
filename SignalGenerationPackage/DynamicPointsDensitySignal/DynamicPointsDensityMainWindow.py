from SignalGenerationPackage.SignalMainWindow import SignalMainWindow
from SignalGenerationPackage.DynamicPointsDensitySignal.Ui_DynamicPointsDensitySignalWindow import Ui_DynamicPointsDensitySignalWindow
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityUIParameters import DynamicPointsDensityUIParameters

class DynamicPointsDensityMainWindow(SignalMainWindow):
    def __init__(self):
        super().__init__()

    # overridden
    def init_plot_title(self):
        self.plot_title = 'Trapezoid (dynamic points density)'

    # overridden
    def init_plot_sizes(self):
        self.plot_height = DynamicPointsDensityUIParameters.PlotHeight
        self.plot_width = DynamicPointsDensityUIParameters.PlotWidth

    # overridden
    def init_plot_positions(self):
        self.plot_pos_x = DynamicPointsDensityUIParameters.PlotXPosition
        self.plot_pos_y = DynamicPointsDensityUIParameters.PlotYPosition

    # overridden
    def init_user_interface(self):
        self.user_interface = Ui_DynamicPointsDensitySignalWindow()