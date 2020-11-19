from SignalGenerationPackage.SignalObserver import SignalObserver
import matplotlib.pyplot as plt

class SinusObserver(SignalObserver):

    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)

    def UpdateModel(self):
        self.plot_canvas.plot(
            self.model.x,
            self.model.y,
            #title='Sinus',
            #labels=['x', 'y'],
            color='blue',
            marker='.'
        )








