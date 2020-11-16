from SignalGenerationPackage.SignalData import SignalData


class DynamicPointsDensitySignalData(SignalData):

    def __init__(self):
        super().__init__()
        self.VerticalOffset = 0

        self.StartTime = 0
        self.AccelerationTime = 0
        self.PlateauTime = 0
        self.DecelerationTime = 0
        self.EndTime = 0

        self.X_from = 0
        self.LowLevelFrequency = 0
        self.HighLevelFrequency = 0
        self.PointsDensity = 0

        self.CriticalAccelerationTangent = 1.6  # Hz per second
        self.CriticalDecelerationTangent = -1.6  # Hz per second
