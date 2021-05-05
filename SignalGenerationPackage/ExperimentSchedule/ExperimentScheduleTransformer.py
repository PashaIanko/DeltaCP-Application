from SignalGenerationPackage.SignalTransformer import SignalTransformer


class ExperimentScheduleTransformer(SignalTransformer):
    def __init__(self, SignalData):
        super().__init__(SignalData)

    # overridden
    def TransformSignal(self):
        pass