import matplotlib.pyplot as plt


class SignalVisualizer:
    def __init__(self):
        self.Figure = plt.figure()
        self.Graph = plt.subplot(111)
        self.Graph.set_title('SENDING Voltage (Flowrate) VS Time')
        self.Graph.set_xlabel('Time, sec')
        self.Graph.set_ylabel('Voltage amplitude, V')
        self.x = []
        self.y = []
        self.actual_freq = []

    def UpdateSetFrequency(self, x_val, y_val):
        self.x.append(x_val)
        self.y.append(y_val)
        self.Graph.plot(self.x, self.y, color='b', marker='.')
        self.Figure.show()

    def UpdateCurrentFrequency(self, x_val, y_val):
        self.actual_freq.append(y_val)
        self.Graph.plot(self.x, self.actual_freq, color='r', marker='.')


    def Restart(self):
        self.x.clear()
        self.y.clear()
        self.Graph.clear()