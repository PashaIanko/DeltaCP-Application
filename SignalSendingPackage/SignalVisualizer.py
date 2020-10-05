import matplotlib.pyplot as plt


class SignalVisualizer:
    def __init__(self, x_arr=[], y_arr=[]):
        self.Figure = plt.figure()
        self.Figure.canvas.mpl_connect('close_event', self.HandleCloseEvent)
        self.Graph = plt.subplot(111)
        self.Graph.set_title('SENDING Voltage (Flowrate) VS Time')
        self.Graph.set_xlabel('Time, sec')
        self.Graph.set_ylabel('Voltage amplitude, V')
        self.x = x_arr
        self.y = y_arr


    def UpdateSetFrequency(self, x_val, y_val):
        self.Graph.plot(self.x, self.y, color='b', marker='.')
        self.Graph.plot(x_val, y_val, 'r+', markersize=5)
        self.Figure.show()

    def UpdateCurrentFrequency(self, x_val, y_val):
        #self.actual_freq.append(y_val)
        if x_val is not None and y_val is not None:
            self.Graph.plot(x_val, y_val, color='yellow', marker='.')

    def HandleCloseEvent(self, evt):
        print('closed figure')
        self.Figure = plt.figure()

    def Restart(self, TimeArray):
        if len(TimeArray) != 0:
            self.x = TimeArray
            self.Graph.set_xlim(self.x[0], self.x[-1])

    def RefreshData(self, x, y):
        self.x = x
        self.y = y
