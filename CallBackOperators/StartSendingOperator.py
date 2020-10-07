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
        self.CommandExecutionTime = 0.02  # Часть времени уходит на исполнение команды (отправку частоты на
                                        # частотник, обновление отрисовки). Надо подобрать этот параметр,
                                        # и начинать исполнение команды на dt раньше, чтобы учесть задержку по времени
                                        # на исполнение команды



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
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        DeltaTimes = SignalData.dx
        N = len(DeltaTimes)
        print(f'len Delta times = {N}, DeltaTime = {DeltaTimes[0]}')
        self.Timer.interval = DeltaTimes[0]
        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 0
        self.TimeStamp = Time[self.PointsIterator]
        self.ValueToSend = SignalData.y[self.PointsIterator]

        self.Timer.run()
        print(f'After Timer run')

        if N != 1:  # If the Time array has only one point, then we've already accomplished it in
                    # the method self.Timer.run()
            i = 0
            i_limit = N - 1
            while i < i_limit:
                #print(f'inside while')
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False
                    i += 1
                    self.PointsIterator += 1

                    print(f'Points Iterator = {self.PointsIterator}')
                    self.ValueToSend = SignalData.y[self.PointsIterator]
                    self.TimeStamp = Time[self.PointsIterator]
                    self.Timer.reset(DeltaTimes[i])

                if self.SendingStopped:
                    print('Stop push button --> finishing thread execution')
                    return

        #self.CycleFinishedSuccessfully = True
        #print(f'Finished CYCLE!')
        while True:
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                print(f'Finished CYCLE!')
                return
        # TODO: Медленно работает, если частота отправки > раза в секунду. Оптимизировать

    def ThreadFunc(self):
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        # TODO: Check that TimeFrom <= TimeTo
        Time = SignalData.x.copy()
        self.SignalVisualizer.RefreshData(SignalData.x, SignalData.y)
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
                    Time[i] += upd_val + SignalData.dx[i]
                self.RestartSignalIterator()
                self.RestartVisualization(Time)
                self.ExecuteSending(Time)


    def RestartVisualization(self, TimeArray):
        print(f'Restarting Visualization!!')
        self.SignalVisualizer.Restart(TimeArray)






    def LaunchSendingThread(self):
        self.SendingThread = Thread(target=self.ThreadFunc)
        self.SendingThread.start()




    def StartSendingSignal(self):
        if self.SendingThread is None:
            print(f'launching thread')
            self.DeltaCPClient.SendStart()
            self.LaunchSendingThread()
        else:
            if not self.SendingThread.is_alive():
                print(f'launching thread')
                self.SignalVisualizer.Restart(TimeArray=[])
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
        print(f'Inside Timer Function')
        value_to_send = int(self.ValueToSend * 100)  # Привести к инту, иначе pymodbus выдаёт ошибку
        self.DeltaCPClient.SetFrequency(value_to_send)
        CurrentFreq = self.DeltaCPClient.RequestCurrentFrequency()
        self.SignalVisualizer.UpdateSetFrequency(self.TimeStamp, self.ValueToSend)
        self.SignalVisualizer.UpdateCurrentFrequency(self.TimeStamp, CurrentFreq)

        self.FunctionWasCalled = True




