from SignalGenerationPackage.Sinus.Ui_SinusMainWindow import Ui_SinusMainWindow
from SignalGenerationPackage.Sinus.SinusUIParameters import SinusUIParameters
from SignalGenerationPackage.SignalMainWindow import SignalMainWindow


class SinusMainWindow(SignalMainWindow):
    def __init__(self):
        super().__init__()

    # overridden
    def init_plot_title(self):
        self.plot_title = 'Sinus signal'

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

    # overridden
    def init_plot(self):
        self.plot = self.user_interface.frame # Это виджет из QtDesigner.
        # Делал интерфейс с помощью этой программы. Там, если открыть .ui файл
        # C помощью qt designer - таm будет виджет frame. Можно открыть
        # класс Ui_SinMainWindow и посмотреть что frame это объект PlotCanvas -
        # как раз наш график

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
    def get_endless_send_checkbox(self):
        return self.user_interface.EndlessSendingradioButton

    # overridden
    def get_cycles_number_widget(self):
        return self.user_interface.CyclesNumberspinBox

    # overridden
    def get_cycle_send_checkbox(self):
        return self.user_interface.radioButton