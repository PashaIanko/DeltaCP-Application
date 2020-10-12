from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.UserSignal.UserSignalData import UserSignalData
from SignalGenerationPackage.SignalData import SignalData
import numpy as np
import statistics


class UserSignal(Signal):

    # Model in MVC pattern
    def __repr__(self):
        print(f'UserSignal in __repr__ method')


    def __init__(self):
        super().__init__()


    def InitSignalData(self):
        self.SignalData = UserSignalData()

    def Func(self, x):
        return abs(self.SignalData.Amplitude * np.sin(self.SignalData.Omega * x + self.SignalData.Phase))

    def UpdateSignalData(self):
        print('updating SignalData')
        SignalData.x = np.linspace(self.SignalData.X_from, self.SignalData.X_to, self.SignalData.PointsNumber,
                                   endpoint=True)  # Пересчёт ГЛОБАЛЬНЫХ Переменных
        SignalData.y = [self.Func(x) for x in SignalData.x]  # TODO: X_From, X_To запихать в родителя


