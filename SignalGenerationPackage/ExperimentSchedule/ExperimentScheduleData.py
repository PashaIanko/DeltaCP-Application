from SignalGenerationPackage.SignalData import SignalData


class ExperimentScheduleData(SignalData):
    def __init__(self):
        super().__init__()

        self.frequencies = []  # Держать частоту self.frequencies[i]
        self.seconds = []       # в течение self.seconds[i] секунд
        self.request_every_N_sec = 1  # Один из параметров ексель файла. Установил в 1, чтобы
        # не было проблем с делением на ноль в ходе подгрузки сигнала из ексель файла (когда
        # частоты и секунды уже считаны, а частота опроса нет, но сигнал уже необходимо пересчитать по
        # MVC паттерну)
        self.whole_length = 0