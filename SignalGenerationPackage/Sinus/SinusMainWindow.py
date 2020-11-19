from SignalGenerationPackage.Sinus.Ui_SinusMainWindow import Ui_SinusMainWindow
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from SignalGenerationPackage.SignalMainWindow import SignalMainWindow


class SinusMainWindow(SignalMainWindow):
    def __init__(self):
        super().__init__()

    # overridden
    def init_plot_sizes(self):
        self.plot_height = SinusUIParameters.SinusPlotHeight
        self.plot_width = SinusUIParameters.SinusPlotWidth

    # overridden
    def init_plot_positions(self):
        self.plot_pos_x = SinusUIParameters.SinusPlotXPosition
        self.plot_pos_y = SinusUIParameters.SinusPlotYPosition

    # overridden
    def init_user_interface(self):
        self.user_interface = Ui_SinusMainWindow()