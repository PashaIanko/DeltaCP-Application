from CallBackOperator import CallBackOperator
from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalTimer import SignalTimer
import time
import sys

class StartSendingOperator(CallBackOperator):

    def __init__(self):
        self.UserInterface = None  # TODO: Перенести в родительский класс UserInterface
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        self.FunctionWasCalled = False


    def ConnectCallBack(self, UserInterface):
        self.UserInterface = UserInterface
        UserInterface.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)


    def StartSendingSignal(self):
        print(SignalData.x, SignalData.y)
        Signal = SignalData.x.copy()
        Time = SignalData.y.copy()
        N = len(Time)
        DeltaTimes = [1, 2, 3, 4, 5]  # [dt_next - dt_prev for dt_next, dt_prev in zip(range(1, N), range(0, N-1))]

        print(f' start: {time.asctime()}')
        self.Timer.reset(DeltaTimes[0])
        try:
            i = 0
            while True:
                if self.FunctionWasCalled:
                    i += 1
                    self.FunctionWasCalled = False
                    self.Timer.reset(DeltaTimes[i])
                if i == len(DeltaTimes) - 1:
                    break
            print('Finished Succeeded')
        except:
            print(sys.exc_info())

    def TestTimer(self):
        print('Test', time.asctime())
        self.FunctionWasCalled = True




