from CallBackOperator import CallBackOperator
from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalTimer import SignalTimer
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from threading import Thread
from DeltaCPClient import DeltaCPClient
import time
import sys


class StartSendingOperator(CallBackOperator):

    def __init__(self):
        self.UserInterface = None  # TODO: Перенести в родительский класс UserInterface
        self.TimeStamp = 0
        self.ValueToSend = 0
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        self.DeltaCPClient = DeltaCPClient()
        self.FunctionWasCalled = False
        self.SendingThreadWasLaunched = False
        self.SendingThread = None  # Поток, в котором отправляем данные сигнала
        self.SignalVisualizer = SignalVisualizer()
        self.PointsIterator = 0  # Just Counter to iterate over [x, y] arrays of SignalData
        self.SendingOnPause = False
        self.SendingStopped = False
        self.EndlessSendingEnabled = False
        self.CycleFinishedSuccessfully = False



    def ConnectCallBack(self, UserInterface):
        self.UserInterface = UserInterface
        UserInterface.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)
        UserInterface.PauseSendingradioButton.toggled.connect(self.PauseSending)
        UserInterface.ResumeSendingradioButton.toggled.connect(self.ResumeSending)
        UserInterface.pushButtonStopSignalSending.clicked.connect(self.StopSendingSignal)
        UserInterface.EndlessSendingcheckBox.stateChanged.connect(lambda: self.EnableEndlessSending())


    def EnableEndlessSending(self):
        self.EndlessSendingEnabled = \
            self.UserInterface.EndlessSendingcheckBox.isChecked()
        print(f'EndlessSendingEnabled = {self.EndlessSendingEnabled}')

    def PauseSending(self):
        if self.UserInterface.PauseSendingradioButton.isChecked():
            print('Paused')
            self.SendingOnPause = True
            self.UserInterface.ResumeSendingradioButton.setChecked(False)
        else:
            self.UserInterface.ResumeSendingradioButton.setChecked(True)

    def ResumeSending(self):
        if self.UserInterface.ResumeSendingradioButton.isChecked():
            print('Resumed')
            self.SendingOnPause = False
            self.UserInterface.PauseSendingradioButton.setChecked(False)
        else:
            self.UserInterface.PauseSendingradioButton.setChecked(True)

    def ExecuteSending(self, Time):
        N = len(Time)
        DeltaTimes = []  # Array consists of dt's. After each dt in the array we execute
        # Sending a new value to DeltaPc
        if N == 0:
            print('no points to send')
            return  # No points at all
        elif N == 1:
            DeltaTimes.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00
        else:
            DeltaTimes = [Time[dt_next_idx] - Time[dt_prev_idx]
                          for dt_next_idx, dt_prev_idx
                          in zip(range(1, N), range(0, N - 1))]
            DeltaTimes.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00
            # TODO: Расчёт DeltaTimes перенести в методы MVC паттерна

        self.Timer.interval = DeltaTimes[0]
        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 0
        self.TimeStamp = Time[self.PointsIterator]
        self.ValueToSend = SignalData.y[self.PointsIterator]
        self.Timer.run()


        if N != 1:  # If the Time array has only one point, then we've already accomplished it in
            # the method self.Timer.run()
            i = 0
            i_limit = len(DeltaTimes) - 1
            while i < i_limit:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False
                    i += 1
                    self.Timer.reset(DeltaTimes[i])
                    self.PointsIterator += 1
                    self.ValueToSend = SignalData.y[self.PointsIterator]
                    self.TimeStamp = Time[self.PointsIterator]

                if self.SendingStopped:
                    print('Stop push button --> finishing thread execution')
                    return
        self.CycleFinishedSuccessfully = True
        return
        # TODO: Медленно работает, если частота отправки > раза в секунду. Оптимизировать

    def ThreadFunc(self):
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        # TODO: Check that TimeFrom <= TimeTo
        Time = SignalData.x.copy()
        self.ExecuteSending(Time)
        while True:
            if self.SendingStopped == True:
                self.SendingStopped = False  # Reset the flag
                return
            elif self.EndlessSendingEnabled and self.CycleFinishedSuccessfully:
                # update Time array and restart the cycle
                self.CycleFinishedSuccessfully = False
                upd_val = SignalData.x[-1]
                for i in range(len(Time)):
                    Time[i] += upd_val
                self.RestartSignalIterator()
                self.ExecuteSending(Time)





    def LaunchSendingThread(self):
        self.SendingThread = Thread(target=self.ThreadFunc)
        self.SendingThread.start()




    def StartSendingSignal(self):
        if self.SendingThread is None:
            print(f'launching thread')
            self.LaunchSendingThread()
        else:
            if not self.SendingThread.is_alive():
                print(f'launching thread')
                self.SignalVisualizer.Restart()
                self.RestartSignalIterator()
                self.SendingStopped = False  # Надо почистить этот флаг
                self.LaunchSendingThread()
            else:
                print(f'Prev sending thread is executing, cant launch one')

    def StopSendingSignal(self):
        self.DeltaCPClient.SetFrequency(0.0)
        self.DeltaCPClient.SendStop()
        self.SendingStopped = True

    def RestartSignalIterator(self):
        self.PointsIterator = 0

    def TestTimer(self):
        self.DeltaCPClient.SetFrequency(self.ValueToSend)
        self.SignalVisualizer.UpdateVisualization(self.TimeStamp, self.ValueToSend)
        self.FunctionWasCalled = True




