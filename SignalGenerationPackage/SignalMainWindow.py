from PyQt5 import QtWidgets
from abc import ABC, abstractmethod
from PlotCanvas import PlotCanvas


class SignalMainWindow(ABC):
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()

        # plot parameters
        self.plot = None
        self.plot_width = 0
        self.plot_height = 0
        self.plot_pos_x = 0
        self.plot_pos_y = 0
        self.user_interface = None
        self.plot_title = 'No title'

        # Процедура конструктора
        self.init_plot_positions()
        self.init_plot_sizes()
        self.init_plot_title()
        self.init_user_interface()  # TODO: self.UserInterface и прочие атрибуты должны хотя бы None быть объявлены в родителе
        self.setup_user_interface()
        self.init_plot()


    @abstractmethod
    def init_plot_title(self):
        pass

    @abstractmethod
    def init_plot_sizes(self):
        pass  # width, height

    @abstractmethod
    def init_plot_positions(self):
        pass  # pos_x, pos_y

    @abstractmethod
    def init_user_interface(self):
        pass

    @abstractmethod
    def init_plot(self):
        pass

    @abstractmethod
    def get_start_button(self):
        pass

    @abstractmethod
    def get_pause_radio_button(self):
        pass

    @abstractmethod
    def get_resume_radio_button(self):
        pass

    @abstractmethod
    def get_stop_button(self):
        pass

    @abstractmethod
    def get_endless_send_radiobutton(self):
        pass

    @abstractmethod
    def get_cycle_send_radiobutton(self):
        pass

    @abstractmethod
    def get_cycles_number_widget(self):
        pass

    @abstractmethod
    def get_LCD_display(self):
        pass

    @abstractmethod
    def get_log_filename_lineedit(self):
        pass

    def setup_user_interface(self):
        self.user_interface.setupUi(self.main_window)

    def show(self):
        self.main_window.show()
