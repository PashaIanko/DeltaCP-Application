from SignalGenerationPackage.SignalData import SignalData


class ExperimentScheduleData(SignalData):
    def __init__(self):
        super().__init__()

        self.frequencies = []  # Держать частоту self.frequencies[i]
        self.seconds = []       # в течение self.seconds[i] секунд
        self.request_every_N_sec = 0  # Один из параметров ексель файла