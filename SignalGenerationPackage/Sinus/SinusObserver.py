from SignalGenerationPackage.SignalObserver import SignalObserver
import matplotlib.pyplot as plt

class SinusObserver(SignalObserver):

    # Это View в модели MVC

    def __init__(self, Controller, Model):
        super().__init__(Controller, Model)
        self.Figure = plt.figure()
        self.Graph = self.Figure.add_subplot(111)



    # overriden method
    def UpdateModel(self):
        self.Graph.clear()
        self.Graph.plot(self.Model.x, self.Model.y, marker = '.')

        plt.title('Voltage (Flowrate) VS Time')
        plt.ylabel('Voltage amplitude, V')
        plt.xlabel('Time, sec')
        plt.show()








