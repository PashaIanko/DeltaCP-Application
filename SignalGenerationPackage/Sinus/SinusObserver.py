from SignalGenerationPackage.SignalObserver import SignalObserver

class SinusObserver(SignalObserver):

    def __init__(self, Controller, Model):
        super().__init__()
        self.Controller = Controller
        self.Model = Model
        self.Model.AddObserver(self)

    # overriden method
    def UpdateModel(self):
        print(f'sinus model changed! Show Updates, amplt = {self.Model.amplitude}')



