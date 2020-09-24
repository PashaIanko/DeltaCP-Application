import matplotlib.pyplot as plt


class SignalVisualizer:
    def __init__(self):
        self.Figure = plt.figure()
        self.Graph = self.Figure.add_subplot(111)
        self.x = []
        self.y = []

    def UpdateVisualization(self, x_val, y_val):
        self.x.append(x_val)
        self.y.append(y_val)

        self.Graph.clear()
        self.Graph.plot(self.x, self.y, marker='.')
        plt.title('SENDING Voltage (Flowrate) VS Time')
        plt.ylabel('Voltage amplitude, V')
        plt.xlabel('Time, sec')
        self.Figure.show()