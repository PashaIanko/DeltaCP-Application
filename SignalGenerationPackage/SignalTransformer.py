from abc import ABC, abstractmethod


class SignalTransformer(ABC):
    def __init__(self, SignalData):
        self.SignalData = SignalData

    @abstractmethod
    def TransformSignal(self):
        pass