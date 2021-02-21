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

    # overridden
    def get_endless_send_radiobutton(self):
        return self.user_interface.EndlessSendingradioButton

    # overridden
    def get_cycle_send_radiobutton(self):
        return self.user_interface.SendCyclesradioButton

    # overridden
    def get_cycles_number_widget(self):
        return self.user_interface.CyclesNumberspinBox


