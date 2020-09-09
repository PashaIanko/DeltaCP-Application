from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.Sinus.SinusData import SinusData
import numpy as np

class SinusSignal(Signal):

    def __repr__(self):
        print(f'ampl = {self.amplitude}, phase = {self.phase}, N = {self.PointsNumber}, '
              f'X_from = {self.X_from}, X_to = {self.X_to}, '
              f'omega = {self.omega}, x = {self.x}, y = {self.y}')




    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        self.SignalData = SinusData()

    def Func(self, x):
        return self.SignalData.Amplitude * np.sin(self.SignalData.Omega * x + self.SignalData.Phase)

    def RecalcData(self):
        self.SignalData.x = np.linspace(self.SignalData.X_from, self.SignalData.X_to, self.SignalData.PointsNumber)
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

    @property
    def X_from(self):
        return self.SignalData.X_from

    @X_from.setter
    def X_from(self, value):
        self.SignalData.X_from = value
        self.RecalcData()
        self.NotifyObservers()

    @property
    def X_to(self):
        return self.SignalData.X_to

    @X_to.setter
    def X_to(self, value):
        self.SignalData.X_to = value
        self.RecalcData()
        self.NotifyObservers()

    @property
    def PointsNumber(self):
        return self.SignalData.PointsNumber

    @PointsNumber.setter
    def PointsNumber(self, value):
        self.SignalData.PointsNumber = value
        self.RecalcData()
        self.NotifyObservers()




