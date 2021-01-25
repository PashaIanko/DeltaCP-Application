from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.DynamicPointsDensitySignal.Ui_DynamicPointsDensitySignalWindow import Ui_DynamicPointsDensitySignalWindow
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignal import DynamicPointsDensitySignal
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignalObserver import DynamicPointsDensitySignalObserver
from SignalGenerationPackage.DynamicPointsDensitySignal.AccelerationTimeCallBackOperator import AccelerationTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DecelerationTimeCallBackOperator import DecelerationTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.HighLevelFrequencyCallBackOperator import HighLevelFrequencyCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.LowLevelFrequencyCallBackOperator import LowLevelFrequencyCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.PlateauTimeCallBackOperator import PlateauTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.PointsDensityCallBackOperator import PointsDensityCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.EndTimeCallBackOperator import EndTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.StartTimeCallBackOperator import StartTimeCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.VerticalOffsetCallBackOperator import VerticalOffsetCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.AutoFillCallBackOperator import AutoFillCallBackOperator
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensityMainWindow import DynamicPointsDensityMainWindow


class DynamicPointsDensitySignalController(SignalController):

    def __init__(self):
        super().__init__()

    # overridden
    def init_model(self):
        self.model = DynamicPointsDensitySignal()

    # overridden
    def init_observer(self):
        self.observer = DynamicPointsDensitySignalObserver(self.model, self.main_window.plot)  # TODO: Посмотри, этот метод везде одинаков, можно в родителя

    # overridden
    def init_main_window(self):
        self.main_window = DynamicPointsDensityMainWindow()

    # overridden
    def init_callback_operators(self):
        import sys
        try:
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
                    PointsDensityCallBackOperator(self.model),
                    AutoFillCallBackOperator(model=None)
                ]
        except:
            print(sys.exc_info())