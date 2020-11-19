import matplotlib.pyplot as plt
from SignalSendingPackage.VisualizerMainWindow import VisualizerMainWindow
import sys

class SignalVisualizer:
    # def __init__(self, x_arr=[], y_arr=[]):
    #     self.Figure = plt.figure()
    #     self.Figure.canvas.mpl_connect('close_event', self.HandleCloseEvent)
    #     self.Graph = self.Figure.add_subplot(111)
    #     self.Graph.set_title('SENDING Voltage (Flowrate) VS Time')
    #     self.Graph.set_xlabel('Time, sec')
    #     self.Graph.set_ylabel('Voltage amplitude, V')
    #     self.x = x_arr
    #     self.y = y_arr
    #     self.Offset = 0.3
    #     self.IfRestarted = True
    #
    # def UpdateSetFrequency(self, x_val, y_val):
    #     self.Graph.plot(x_val, y_val, 'r+', markersize=15)
    #     if self.IfRestarted:
    #         self.IfRestarted = False
    #         self.Graph.plot(self.x, self.y, color='b', marker='.')
    #     self.Figure.show()
    #
    #
    # def UpdateCurrentFrequency(self, x_val, y_val):
    #     if x_val is not None and y_val is not None:
    #         self.Graph.plot(x_val, y_val, color='black', marker='x', markersize=7)
    #
    # def HandleCloseEvent(self, evt):
    #     self.Figure = plt.figure()
    #
    # def Restart(self, TimeArray):
    #     self.Graph.clear()
    #     # Сейчас должны рестартануть. Поэтому, в функции self.UpdateSetFreuency(x, y)
    #     # Мы вызовем функцию plot().
    #     self.IfRestarted = True
    #     if len(TimeArray) != 0:
    #         self.x = TimeArray
    #         self.Graph.set_xlim(TimeArray[0] - self.Offset, TimeArray[-1] + self.Offset)
    #
    # def RefreshData(self, x, y):
    #     self.x = x
    #     self.y = y




    def __init__(self, x_arr=[], y_arr=[]):
        self.main_window = None  # Окно, куда будем выводить визуализацию
        self.init_main_window()
        self.Graph = self.main_window.VisualizerPlot
        self.x = x_arr
        self.y = y_arr
        self.IfRestarted = True
        self.Offset = 0.3

    def init_main_window(self):
        self.main_window = VisualizerMainWindow()
        self.main_window.show()

    def UpdateSetFrequency(self, x_val, y_val):
        if self.IfRestarted:
            self.IfRestarted = False
            self.Graph.plot(self.x, self.y, color='b', marker='.', markersize=7)
            self.Graph.add_point(x_val, y_val, color='red', marker='+', markersize=10)
        else:
            self.Graph.add_point(x_val, y_val, color='red', marker='+', markersize=10)


    def UpdateCurrentFrequency(self, x_val, y_val):
        if x_val is not None and y_val is not None:
            self.Graph.plot(x_val, y_val, color='black', marker='x', markersize=7)

    def Restart(self, TimeArray):
        self.Graph.clear()
        # Сейчас должны рестартануть. Поэтому, в функции self.UpdateSetFreuency(x, y)
        # Мы вызовем функцию plot().
        self.IfRestarted = True
        if len(TimeArray) != 0:
            self.x = TimeArray
            self.Graph.set_xlim(TimeArray[0] - self.Offset, TimeArray[-1] + self.Offset)

    def RefreshData(self, x, y):
        self.x = x
        self.y = y
