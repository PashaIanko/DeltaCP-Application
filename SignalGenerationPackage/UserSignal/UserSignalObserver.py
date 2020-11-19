from SignalGenerationPackage.SignalObserver import SignalObserver
import matplotlib.pyplot as plt

class UserSignalObserver(SignalObserver):

    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)

