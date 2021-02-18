from SignalGenerationPackage.UserSignal.Ui_UserSignalWindow import Ui_UserSignalWindow
from SignalGenerationPackage.UserSignal.UserSignalUIParameters import UserSignalUIParameters
from SignalGenerationPackage.SignalMainWindow import SignalMainWindow


class UserSignalMainWindow(SignalMainWindow):
    def __init__(self):
        super().__init__()

    # overridden
    def init_plot_title(self):
        self.plot_title = 'Trapezoid (constant points density)'

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

    # overridden
    def init_plot(self):
        self.plot = self.user_interface.plot_widget

    # overridden
    def get_start_button(self):
        return self.user_interface.pushButtonStartSignalSending

    # overridden
    def get_pause_radio_button(self):
        return self.user_interface.PauseSendingradioButton

    # overridden
    def get_resume_radio_button(self):
        return self.user_interface.ResumeSendingradioButton

    # overridden
    def get_stop_button(self):
        return self.user_interface.pushButtonStopSignalSending

    def get_endless_send_checkbox(self):
        return self.user_interface.EndlessSendingcheckBox