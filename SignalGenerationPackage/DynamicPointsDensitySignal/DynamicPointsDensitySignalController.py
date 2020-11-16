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


class DynamicPointsDensitySignalController(SignalController):

    def __init__(self):
        super().__init__()


    def InitModel(self):
        # creating MVC model
        self.Model = DynamicPointsDensitySignal()

    def InitView(self):
        self.View = DynamicPointsDensitySignalObserver(self, self.Model)

    def InitSignalUI(self):
        self.UserInterface = Ui_DynamicPointsDensitySignalWindow()

    def InitCallBackOperators(self):
        self.CallbackOperators = \
            [
                StartTimeCallBackOperator(self.Model),
                AccelerationTimeCallBackOperator(self.Model),
                PlateauTimeCallBackOperator(self.Model),
                DecelerationTimeCallBackOperator(self.Model),
                EndTimeCallBackOperator(self.Model),
                VerticalOffsetCallBackOperator(self.Model),
                HighLevelFrequencyCallBackOperator(self.Model),
                LowLevelFrequencyCallBackOperator(self.Model),
                PointsDensityCallBackOperator(self.Model),
                AutoFillCallBackOperator()
            ]

    # overriden
    def ConnectCallBacks(self):
        for operator in self.CallbackOperators:
            operator.ConnectCallBack(self.UserInterface)
