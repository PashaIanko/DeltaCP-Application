from SignalGenerationPackage.EdgeSignal.Ui_EdgeSignalWindow import Ui_EdgeSignalWindow
from SignalGenerationPackage.SignalMainWindow import SignalMainWindow


class EdgeSignalMainWindow(SignalMainWindow):
    def __init__(self):
        super().__init__()

    # overridden
    def init_plot_title(self):
        pass

    # overridden
    def init_plot_sizes(self):
        pass

    # overridden
    def init_plot_positions(self): # TODO: удалить эти plot_* методы
        pass

    # overridden
    def init_user_interface(self):
        self.user_interface = Ui_EdgeSignalWindow()

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

    # overridden
    def get_endless_send_radiobutton(self):
        return self.user_interface.EndlessSendingradioButton

    # overridden
    def get_cycle_send_radiobutton(self):
        return self.user_interface.SendCyclesradioButton

    # overridden
    def get_cycles_number_widget(self):
        return self.user_interface.CyclesNumberspinBox

    # overridden
    def get_LCD_display(self):
        return self.user_interface.lcdNumber

    # overridden
    def get_log_filename_lineedit(self):
        return self.user_interface.LogFilenamelineEdit