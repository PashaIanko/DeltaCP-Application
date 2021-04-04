from PyQt5 import QtWidgets
from abc import ABC, abstractmethod
from PlotCanvas import PlotCanvas


class SignalMainWindow(ABC):
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()

        # plot parameters
        self.plot = None
        self.user_interface = None

        # Процедура конструктора
        self.init_user_interface()  # TODO: self.UserInterface и прочие атрибуты должны хотя бы None быть объявлены в родителе
        self.setup_user_interface()
        self.init_plot()




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
