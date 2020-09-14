from CallBackOperator import CallBackOperator
from SignalGenerationPackage.SignalData import SignalData

class StartSendingOperator(CallBackOperator):

    def __init__(self):
        self.UserInterface = None  # TODO: Перенести в родительский класс UserInterface


    def ConnectCallBack(self, UserInterface):
        self.UserInterface = UserInterface
        UserInterface.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)


    def StartSendingSignal(self):
        print(SignalData.x, SignalData.y)
        Signal = SignalData.x.copy()
        Time = SignalData.y.copy()
