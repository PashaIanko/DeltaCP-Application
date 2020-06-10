from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.Sinus.SinusData import SinusData

class SinusSignal(Signal):

    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        self.SignalData = SinusData()

    def Func(self):
        pass  # return A * sin(w * t + phi)


    @property
    def amplitude(self):
        return self.SignalData.Amplitude

    @amplitude.setter
    def amplitude(self, value):
        self.SignalData.Amplitude = value
        self.NotifyObservers()

    @property
    def omega(self):
        return self.SignalData.Omega

    @omega.setter
    def omega(self, value):
        self.SignalData.Omega = value
        self.NotifyObservers()

    @property
    def phase(self):
        return self.SignalData.Phase

    @phase.setter
    def phase(self, value):
        self.SignalData.Phase = value
        self.NotifyObservers()


