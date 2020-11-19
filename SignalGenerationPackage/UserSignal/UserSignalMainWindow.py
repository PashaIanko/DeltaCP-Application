from SignalGenerationPackage.UserSignal.Ui_UserSignalWindow import Ui_UserSignalWindow
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters
from SignalGenerationPackage.SignalMainWindow import SignalMainWindow


class UserSignalMainWindow(SignalMainWindow):
    def __init__(self):
        super().__init__()

    # overridden
    def init_plot_sizes(self):
        self.plot_height = UserSignalUIParameters.PlotHeight
        self.plot_width = UserSignalUIParameters.PlotWidth

    # overridden
    def init_plot_positions(self):
        self.plot_pos_x = UserSignalUIParameters.PlotXPosition
        self.plot_pos_y = UserSignalUIParameters.PlotYPosition

    # overridden
    def init_user_interface(self):
        self.user_interface = Ui_UserSignalWindow()