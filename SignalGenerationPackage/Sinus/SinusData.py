from SignalGenerationPackage.SignalData import SignalData


class SinusData(SignalData):

    def __init__(self):
        super().__init__()
        self.Omega = 0
        self.Amplitude = 0
        self.Phase = 0
        self.X_from = 0
        self.X_to = 0
        self.PointsNumber = 0



