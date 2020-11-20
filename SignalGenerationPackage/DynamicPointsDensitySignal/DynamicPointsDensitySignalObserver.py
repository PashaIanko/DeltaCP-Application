from SignalGenerationPackage.SignalObserver import SignalObserver


class DynamicPointsDensitySignalObserver(SignalObserver):

    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)
