from SignalGenerationPackage.SignalController import  SignalController
from SignalGenerationPackage.UserSignal.Ui_UserSignalWindow import Ui_UserSignalWindow
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


class UserSignalController(SignalController):

    def __init__(self):
        super().__init__()


    def InitModel(self):
        # creating MVC model
        self.Model = UserSignal()

    def InitView(self):
        # creating MVC view
        self.View = UserSignalObserver(self, self.Model)

    # overriden method - here you define personal Graphical Interface
    # (Ui) and show the window
    def InitSignalUI(self):
        self.UserInterface = Ui_UserSignalWindow()

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
                PointsNumberCallBackOperator(self.Model)
            ]

    # overriden
    def ConnectCallBacks(self):
        for operator in self.CallbackOperators:
            operator.ConnectCallBack(self.UserInterface)
