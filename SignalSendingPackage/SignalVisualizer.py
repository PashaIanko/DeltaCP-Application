import matplotlib.pyplot as plt


class SignalVisualizer:
    def __init__(self):
        self.Figure = plt.figure()
        self.Graph = plt.subplot(111)
        self.Graph.set_title('SENDING Voltage (Flowrate) VS Time')
        self.Graph.set_xlabel('Time, sec')
        self.Graph.set_ylabel('Voltage amplitude, V')

    def UpdateVisualization(self, x_val, y_val):
        self.Graph.plot(x_val, y_val, color='b', marker='.')
        self.Figure.show()