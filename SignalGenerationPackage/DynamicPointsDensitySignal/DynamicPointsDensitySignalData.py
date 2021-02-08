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

        self.CriticalAccelerationTangent = 2.5  # Hz per second
        self.CriticalDecelerationTangent = -2.5  # Hz per second

        # Это константа для подгонки плотности точек, чтобы ЧП разгонялся не слишком быстро и не слишком медленно
        self.FittingConstant = 8.0

        # Ограничение на максимальную плотность точек, чтоб сплошняком не подавать,
        # слишком часто мы не можем
        self.MaxPointsDensity = 1.0
