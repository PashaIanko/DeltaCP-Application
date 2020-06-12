from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.Sinus.SinusData import SinusData
import numpy as np

class SinusSignal(Signal):

    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        self.SignalData = SinusData()

    def Func(self, x):
        return self.SignalData.Amplitude * np.sin(self.SignalData.Omega * x + self.SignalData.Phase)

    def RecalcData(self):
        self.SignalData.x = np.linspace(self.SignalData.x_from, self.SignalData.x_to, self.SignalData.points_numb)
        self.SignalData.y = [self.Func(x) for x in self.SignalData.x]

    @property
    def amplitude(self):
        return self.SignalData.Amplitude

    @amplitude.setter
    def amplitude(self, value):
        self.SignalData.Amplitude = value
        self.RecalcData()
        self.NotifyObservers()

    @property
    def omega(self):
        return self.SignalData.Omega

    @omega.setter
    def omega(self, value):
        self.SignalData.Omega = value
        self.RecalcData()
        self.NotifyObservers()

    @property
    def phase(self):
        return self.SignalData.Phase

    @phase.setter
    def phase(self, value):
        self.SignalData.Phase = value
        self.RecalcData()
        self.NotifyObservers()

    @property
    def x(self):
        return self.SignalData.x

    @property
    def y(self):
        return self.SignalData.y


