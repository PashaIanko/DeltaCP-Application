from SignalGenerationPackage.Signal import Signal
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleData import ExperimentScheduleData
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleTransformer import ExperimentScheduleTransformer


class ExperimentScheduleModel(Signal):

    # Model in MVC pattern

    def __init__(self):
        super().__init__()

    # overridden
    def InitSendingTransformer(self):
        self.SendingTransformer = ExperimentScheduleTransformer(self.SignalData)

    # overridden
    def InitSignalData(self):
        self.SignalData = ExperimentScheduleData()

    # overridden
    def Func(self, x):
        pass

    # overridden
    def UpdateSignalData(self):
        print(f'In UpdateSignalData')

    # overridden
    def AddRequests_Y(self):
        pass