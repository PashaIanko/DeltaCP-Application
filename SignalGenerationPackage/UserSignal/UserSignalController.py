from SignalGenerationPackage.SignalController import  SignalController
from SignalGenerationPackage.UserSignal.UserSignal import UserSignal
from SignalGenerationPackage.UserSignal.UserSignalObserver import UserSignalObserver
from SignalGenerationPackage.UserSignal.AccelerationTimeCallBackOperator import AccelerationTimeCallBackOperator
from SignalGenerationPackage.UserSignal.DecelerationTimeCallBackOperator import DecelerationTimeCallBackOperator
from SignalGenerationPackage.UserSignal.HighLevelFrequencyCallBackOperator import HighLevelFrequencyCallBackOperator
from SignalGenerationPackage.UserSignal.LowLevelFrequencyCallBackOperator import LowLevelFrequencyCallBackOperator
from SignalGenerationPackage.UserSignal.PlateauTimeCallBackOperator import PlateauTimeCallBackOperator
from SignalGenerationPackage.UserSignal.PointsNumberCallBackOperator import PointsNumberCallBackOperator
from SignalGenerationPackage.UserSignal.EndTimeCallBackOperator import EndTimeCallBackOperator
from SignalGenerationPackage.UserSignal.StartTimeCallBackOperator import StartTimeCallBackOperator
from SignalGenerationPackage.UserSignal.VerticalOffsetCallBackOperator import VerticalOffsetCallBackOperator
from SignalGenerationPackage.UserSignal.AutoFillCallBackOperator import AutoFillCallBackOperator
from SignalGenerationPackage.UserSignal.UserSignalMainWindow import UserSignalMainWindow

class UserSignalController(SignalController):

    def __init__(self):
        super().__init__()


    def init_model(self):
        self.model = UserSignal()

    def init_observer(self):
        self.observer = UserSignalObserver(self.model, self.main_window.plot)

    def init_main_window(self):
        self.main_window = UserSignalMainWindow()

    def init_callback_operators(self):
        self.callback_operators = \
            [
                StartTimeCallBackOperator(self.model),
                AccelerationTimeCallBackOperator(self.model),
                PlateauTimeCallBackOperator(self.model),
                DecelerationTimeCallBackOperator(self.model),
                EndTimeCallBackOperator(self.model),
                VerticalOffsetCallBackOperator(self.model),
                HighLevelFrequencyCallBackOperator(self.model),
                LowLevelFrequencyCallBackOperator(self.model),
                PointsNumberCallBackOperator(self.model),
                AutoFillCallBackOperator(model=None)
            ]