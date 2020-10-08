import matplotlib.pyplot as plt
import sys

class SignalVisualizer:
    def __init__(self, x_arr=[], y_arr=[]):
        self.Figure = plt.figure()
        self.Figure.canvas.mpl_connect('close_event', self.HandleCloseEvent)
        self.Graph = self.Figure.add_subplot(111)
        self.Graph.set_title('SENDING Voltage (Flowrate) VS Time')
        self.Graph.set_xlabel('Time, sec')
        self.Graph.set_ylabel('Voltage amplitude, V')
        self.x = x_arr
        self.y = y_arr
        self.Offset = 0.3

    def UpdateSetFrequency(self, x_val, y_val):
        self.Graph.plot(x_val, y_val, 'r+', markersize=15)
        self.Graph.plot(self.x, self.y, color='b', marker='.')
        self.Figure.show()

    def UpdateCurrentFrequency(self, x_val, y_val):
        if x_val is not None and y_val is not None:
            self.Graph.plot(x_val, y_val, color='yellow', marker='.')

    def HandleCloseEvent(self, evt):
        self.Figure = plt.figure()

    def Restart(self, TimeArray):
        #self.Graph.clear()
        if len(TimeArray) != 0:
            self.x = TimeArray
            self.Graph.set_xlim(self.x[0] - self.Offset, self.x[-1] + self.Offset)

    def RefreshData(self, x, y):
        self.x = x
        self.y = y
