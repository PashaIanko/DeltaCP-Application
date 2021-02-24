from SignalGenerationPackage.SignalData import SignalData


class EdgeSignalData(SignalData):

    def __init__(self):
        super().__init__()

        self.StartTime = 0
        self.AccelerationTime = 0
        self.PlateauTime = 0
        self.DecelerationTime = 0
        self.EndTime = 0

        self.LowLevelFrequency = 0
        self.HighLevelFrequency = 0