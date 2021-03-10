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

        # Необходимые времёна разгона для
        # Частотного преобразователя
        self.MinFrequency = 0
        self.MaxFrequency = 50
        self.NecessaryAccelerationTime = 0
        self.NecessaryDecelerationTime = 0

        # Критические Параметры разгона
        self.CriticalAcceleration = (self.MaxFrequency - self.MinFrequency) / (15)  # От 0 до 50 Hz за 15 сек
        self.CriticalDeceleration = (self.MaxFrequency - self.MinFrequency) / (15) # От 50 до 0 Hz за 15 сек

        # Ускорение / Замедление (Пересчитывается при редактировании сигнала)
        self.AccelerationCoeff = 0
        self.DecelerationCoeff = 0
