from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None,  width=3.8, height=3.5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)

        self.setStyleSheet("background-color:rgb(240,240,240);")
        self.fig.set_facecolor("none")
        self.axes = self.fig.add_subplot(111)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, x, y, title='', labels=['', ''], **kwargs):
        self.axes.cla()
        self.axes.grid(True, which='both', axis='both')
        self.axes.set_xscale('linear')
        self.axes.set_yscale('linear')
        self.axes.set_title(title)
        self.axes.set(xlabel=labels[0], ylabel=labels[1])
        self.axes.plot(x, y, **kwargs)
        self.fig.canvas.draw_idle()

    def clear(self):
        self.axes.clear()