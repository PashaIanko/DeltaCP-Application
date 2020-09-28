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
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        self.DeltaCPClient = DeltaCPClient()
        self.FunctionWasCalled = False
        self.SendingThreadWasLaunched = False
        self.SendingThread = None  # Поток, в котором отправляем данные сигнала
        self.SignalVisualizer = SignalVisualizer()
        self.PointsIterator = 0  # Just Counter to iterate over [x, y] arrays of SignalData


    def ConnectCallBack(self, UserInterface):
        self.UserInterface = UserInterface
        UserInterface.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)
        UserInterface.PauseSendingradioButton.toggled.connect(self.PauseSending)
        UserInterface.ResumeSendingradioButton.toggled.connect(self.ResumeSending)

    def PauseSending(self):
        if self.UserInterface.PauseSendingradioButton.isChecked():
            self.UserInterface.ResumeSendingradioButton.setChecked(False)
        else:
            self.UserInterface.ResumeSendingradioButton.setChecked(True)

    def ResumeSending(self):
        if self.UserInterface.ResumeSendingradioButton.isChecked():
            self.UserInterface.PauseSendingradioButton.setChecked(False)
        else:
            self.UserInterface.PauseSendingradioButton.setChecked(True)

    def ThreadFunc(self):
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)

        # TODO: Check that TimeFrom <= TimeTo
        Time = SignalData.x  #.copy()
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
                          in zip(range(1, N), range(0, N-1))]
            DeltaTimes.insert(0, 0.0)  # Начальная точка отсчёта по времени, 0.00

        self.Timer.interval = DeltaTimes[0]
        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.Timer.run()

        if N != 1:  # If the Time array has only one point, then we've already accomplished it in
                    # the method self.Timer.run()
            i = 0
            i_limit = len(DeltaTimes) - 1
            while i < i_limit:
                if self.FunctionWasCalled:
                    self.FunctionWasCalled = False
                    i += 1
                    self.Timer.reset(DeltaTimes[i])
        print('Cycle finished successfully!')
        # TODO: Жмёшь StartSignalSending.Жждёшь завершения. Ещё раз жмёшь - баг
        # TODO: Паузу, стоп сделать. Сделать бесконечную отправку.
        # TODO: Медленно работает, если частота отправки > раза в секунду. Оптимизировать



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
                self.LaunchSendingThread()
            else:
                print(f'Prev sending thread is executing, cant launch one')


    def TestTimer(self):
        current_value = SignalData.y[self.PointsIterator]
        time_stamp = SignalData.x[self.PointsIterator]
        self.DeltaCPClient.SetFrequency(current_value)
        self.SignalVisualizer.UpdateVisualization(time_stamp, current_value)
        self.PointsIterator += 1
        self.FunctionWasCalled = True




