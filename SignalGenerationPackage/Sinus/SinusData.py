from SignalGenerationPackage.SignalData import SignalData


class SinusData(SignalData):

    def __init__(self):
        super().__init__()
        self.Omega = 0
        self.Amplitude = 0
        self.Phase = 0

    @property
    def omega(self):
        return self.Omega



    @property
    def phase(self):
        return self.Phase
