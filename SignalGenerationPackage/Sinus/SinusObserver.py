from SignalGenerationPackage.SignalObserver import SignalObserver

class SinusObserver(SignalObserver):

    def __init__(self, Controller, Model):
        super().__init__(Controller, Model)


    # overriden method
    def UpdateModel(self):
        print(f'sinus model changed! Show Updates, amplt = {self.Model.amplitude}')
        print(self.Model.x, self.Model.y)



