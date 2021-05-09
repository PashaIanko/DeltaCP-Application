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

    @property
    def frequencies(self):
        return self.SignalData.frequencies

    @frequencies.setter
    def frequencies(self, freq_arr):
        self.SignalData.frequencies = freq_arr

    @property
    def seconds(self):
        return self.SignalData.seconds

    @seconds.setter
    def seconds(self, seconds_arr):
        self.SignalData.seconds = seconds_arr

    @property
    def request_every_N_sec(self):
        return self.SignalData.request_every_N_sec

    @request_every_N_sec.setter
    def request_every_N_sec(self, val):
        self.SignalData.request_every_N_sec = val