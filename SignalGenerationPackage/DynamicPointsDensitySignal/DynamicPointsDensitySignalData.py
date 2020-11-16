from SignalGenerationPackage.SignalData import SignalData


class DynamicPointsDensitySignalData(SignalData):

    def __init__(self):
        super().__init__()
        self.VerticalOffset = 0

        self.StartTime = 0
        self.AccelerationTime = 0.01  # Чтоб избежать деления на ноль
        self.PlateauTime = 0
        self.DecelerationTime = 0.01  # Чтоб избежать деления на ноль
        self.EndTime = 0

        self.X_from = 0
        self.PointsDensity = 0
        self.LowLevelFrequency = 0
        self.HighLevelFrequency = 0
