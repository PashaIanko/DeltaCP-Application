from SignalGenerationPackage.SignalData import SignalData


class UserSignalData(SignalData):

    def __init__(self):
        super().__init__()
        self.VerticalOffset = 0

        self.StartTime = 0
        self.AccelerationTime = 0.01  # Чтоб избежать деления на ноль
        self.PlateauTime = 0
        self.DecelerationTime = 0.01  # Чтоб избежать деления на ноль
        self.EndTime = 0

        self.X_from = 0
        #self.X_to = 0
        self.PointsNumber = 0
        self.LowLevelFrequency = 0
        self.HighLevelFrequency = 0  # Это не частота сигнала - это частота переменного
                                    # Напряжения на DeltaCP 2000. (LowLevel, HighLevel - минимум и максимум сигнала)
