from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.Sinus.SinusData import SinusData
from SignalGenerationPackage.SignalData import SignalData
import numpy as np


class SinusSignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        print(f'ampl = {self.amplitude}, phase = {self.phase}, N = {self.PointsNumber}, '
              f'X_from = {self.X_from}, X_to = {self.X_to}, '
              f'omega = {self.omega}, x = {self.x}, y = {self.y}')




    def __init__(self):
        super().__init__()

    def InitSignalData(self):
        self.SignalData = SinusData()

    def Func(self, x):
        return abs(self.SignalData.Amplitude * np.sin(self.SignalData.Omega * x + self.SignalData.Phase))

    def UpdateSignalData(self):
        print('updating SignalData')
        SignalData.x = np.linspace(self.SignalData.X_from, self.SignalData.X_to, self.SignalData.PointsNumber,
                                   endpoint=True)  # Пересчёт ГЛОБАЛЬНЫХ Переменных
        SignalData.y = [self.Func(x) for x in SignalData.x]  # TODO: X_From, X_To запихать в родителя

    def UpdateDeltaTimes(self):
        N = len(SignalData.x)
        if N == 0:
            return  # No points at all
        elif N == 1:
            SignalData.dx.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00
        elif N > 1:
            SignalData.dx = [
                SignalData.x[dt_next_idx] - SignalData.x[dt_prev_idx]
                for dt_next_idx, dt_prev_idx
                in zip(range(1, N), range(0, N - 1))
            ]
            SignalData.dx.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00


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
        return SignalData.x #self.SignalData.x # Возвращаются глобальные перем (class attributes) - x и y

    @property
    def y(self):
        return SignalData.y # self.SignalData.y # Возвращаются глобальные перем (class attributes) - x и y

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




