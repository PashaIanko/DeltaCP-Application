from SignalGenerationPackage.SignalObserver import SignalObserver
import matplotlib.pyplot as plt

class SinusObserver(SignalObserver):

    # Это View в модели MVC

    def __init__(self, Controller, Model):
        super().__init__(Controller, Model)

        # plt.ion()
        self.Figure = plt.figure()
        self.Graph = self.Figure.add_subplot(111)
        #self.Plot, = self.Graph.plot(self.Model.x, self.Model.y, marker = '.')
        #self.Figure.show()



    # overriden method
    def UpdateModel(self):
        self.Model.__repr__()
        #  self.Graph.clear()
        #  self.Graph.plot(self.Model.x, self.Model.y, marker = '.')
        #  self.Plot.set_ydata(self.Model.y)
        #  self.Plot.set_xdata(self.Model.x)
        #  self.Figure.canvas.draw()
        self.Graph.clear()
        self.Graph.plot(self.Model.x, self.Model.y)
        plt.show()







