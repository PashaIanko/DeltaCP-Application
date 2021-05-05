from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleData import ExperimentScheduleData
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleTransformer import ExperimentScheduleTransformer


class ExperimentScheduleModel(Signal):
    def __init__(self):
        super().__init__()

    # overridden
    def InitSendingTransformer(self):
        self.SendingTransformer = None

    # overridden
    def InitSignalData(self):
        self.SignalData = ExperimentScheduleData()