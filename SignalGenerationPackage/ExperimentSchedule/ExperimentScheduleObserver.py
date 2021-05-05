from SignalGenerationPackage.SignalObserver import SignalObserver


class ExperimentScheduleObserver(SignalObserver):

    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)