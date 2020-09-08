from SignalGenerationPackage.SignalObserver import SignalObserver
import matplotlib.pyplot as plt

class SinusObserver(SignalObserver):

    # Это View в модели MVC

    def __init__(self, Controller, Model):
        super().__init__(Controller, Model)
        self.Figure = plt.figure()


    # overriden method
    def UpdateModel(self):
        print(f'sinus model changed! Show Updates, amplt = {self.Model.amplitude},'
              f'time from = {self.Model.X_from}')
        print(self.Model.__repr__)
        print(self.Model.x, self.Model.y)



