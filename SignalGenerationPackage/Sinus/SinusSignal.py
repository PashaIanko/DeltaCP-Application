from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.Sinus.SinusData import SinusData

class SinusSignal(Signal):

    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        pass  # self.SignalData = SinusSignalData()
        self.SignalData = SinusData()


    def Plot(self):
        print('plotting changes')


    def Func(self):
        pass