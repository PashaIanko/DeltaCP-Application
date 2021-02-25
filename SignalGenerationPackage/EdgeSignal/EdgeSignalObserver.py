from SignalGenerationPackage.SignalObserver import SignalObserver


class EdgeSignalObserver(SignalObserver):

    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)