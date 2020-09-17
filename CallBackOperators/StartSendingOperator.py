from CallBackOperator import CallBackOperator
from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalTimer import SignalTimer
from threading import Thread
import time
import sys


class StartSendingOperator(CallBackOperator):

    def __init__(self):
        self.UserInterface = None  # TODO: Перенести в родительский класс UserInterface
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        self.FunctionWasCalled = False
        self.SendingThreadWasLaunched = False
        self.SendingThread = None  # Поток, в котором отправляем данные сигнала


    def ConnectCallBack(self, UserInterface):
        self.UserInterface = UserInterface
        UserInterface.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)

    def ThreadFunc(self):
        print(SignalData.x, SignalData.y)
        Signal = SignalData.x.copy()
        Time = SignalData.y.copy()
        N = len(Time)
        DeltaTimes = [1, 2, 3, 4, 5]  # [dt_next - dt_prev for dt_next, dt_prev in zip(range(1, N), range(0, N-1))]

        print(f' start: {time.asctime()}')
        self.Timer.interval = DeltaTimes[0]
        self.Timer.run()
        try:
            i = 0
            while True:
                if self.FunctionWasCalled:
                    self.FunctionWasCalled = False
                    i += 1
                    self.Timer.reset(DeltaTimes[i])
                if i == len(DeltaTimes) - 1:
                    break
        except:
            print(sys.exc_info())


    def StartSendingSignal(self):
        if self.SendingThreadWasLaunched == False:  # Или поток завершился или не был запущен
            self.SendingThreadWasLaunched = True
            self.SendingThread = Thread(target=self.ThreadFunc)
            self.SendingThread.start()  # TODO: Защита, если два раза нажали Start Sending - чтобы два раза поток не запускался
        else:
            pass



    def TestTimer(self):
        print('Test', time.asctime())
        self.FunctionWasCalled = True




