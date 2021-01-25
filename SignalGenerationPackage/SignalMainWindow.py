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
        self.init_plot()
        self.init_user_interface()
        self.setup_user_interface()

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

    def init_plot(self):
        self.plot = PlotCanvas(parent=self.main_window,
                               width=self.plot_width,
                               height=self.plot_height,
                               title=self.plot_title)

        self.plot.move(self.plot_pos_x,
                       self.plot_pos_y)

    def setup_user_interface(self):
        self.user_interface.setupUi(self.main_window)

    def show(self):
        self.main_window.show()
