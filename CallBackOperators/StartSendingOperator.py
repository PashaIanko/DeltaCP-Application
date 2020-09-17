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
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)

        Signal = SignalData.x.copy()
        Time = SignalData.y.copy()
        N = len(Time)
        DeltaTimes = [1, 2, 3]  # [dt_next - dt_prev for dt_next, dt_prev in zip(range(1, N), range(0, N-1))]

        if len(DeltaTimes):
            print(f' start: {time.asctime()}')
            self.Timer.interval = DeltaTimes[0]
            self.Timer.run()
            i = 0
            while True:
                # print('inside while')
                if self.FunctionWasCalled:
                    self.FunctionWasCalled = False
                    i += 1
                    self.Timer.reset(DeltaTimes[i])
                if i == len(DeltaTimes) - 1:
                    break

    def LaunchSendingThread(self):
        self.SendingThread = Thread(target=self.ThreadFunc)
        self.SendingThread.start()


    def StartSendingSignal(self):
        '''if self.SendingThread is None:
            print(f'launching thread')
            self.LaunchSendingThread()
        else:
            if not self.SendingThread.is_alive():
                print(f'launching thread')
                self.LaunchSendingThread()
            else:
                print(f'Prev sending thread is executing, cant launch one')'''

        if self.SendingThreadWasLaunched == False:  # Или поток завершился или не был запущен
            self.SendingThread = Thread(target=self.ThreadFunc)
            self.SendingThread.start()  # TODO: Защита, если два раза нажали Start Sending - чтобы два раза поток не запускался
            self.SendingThreadWasLaunched = True
            print(self.SendingThread.is_alive())
        else:
            print(self.SendingThread.is_alive())



    def TestTimer(self):
        print('Test', time.asctime())
        self.FunctionWasCalled = True




