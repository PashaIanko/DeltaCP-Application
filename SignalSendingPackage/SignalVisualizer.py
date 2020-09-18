import matplotlib.pyplot as plt


class SignalVisualizer:
    def __init__(self):
        self.Figure = plt.figure()
        self.Graph = self.Figure.add_subplot(111)

    def UpdateVisiualization(self):
        pass