from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None,  width=8.8, height=10.5, dpi=100, title='Default title'):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setStyleSheet("background-color:rgb(240,240,240);")
        self.fig.set_facecolor("none")
        self.axes = self.fig.add_subplot(111)
        self.setParent(parent)
        self.title = title
        self.set_up_plot()

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def set_up_plot(self):
        self.axes.cla()
        self.axes.grid(True, which='both', axis='both')
        self.axes.set_xscale('linear')
        self.axes.set_yscale('linear')
        self.axes.set_title(self.title)

    def plot(self, x, y, **kwargs):
        self.axes.cla()
        self.axes.grid(True, which='both', axis='both')
        self.axes.plot(x, y, **kwargs)
        self.fig.canvas.draw_idle()

    def add_point(self, x, y, **kwargs):
        self.axes.plot(x, y, **kwargs)
        self.fig.canvas.draw_idle()

    def clear(self):
        self.axes.cla()
        #self.axes.clear()

    def set_xlim(self, left, right):
        self.axes.set_xlim(left, right)