from CallBackOperator import CallBackOperator
from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalTimer import SignalTimer
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from threading import Thread
from DeltaCPClient import DeltaCPClient
from time import sleep
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

        self.SignalVisualizer = None #SignalVisualizer()
        self.SignalVisualizerConstructed = False

        self.PointsIterator = 0  # Just Counter to iterate over [x, y] arrays of SignalData
        self.SendingOnPause = False
        self.SendingStopped = False
        self.EndlessSendingEnabled = False
        self.IsFirstCycle = True
        self.CycleFinishedSuccessfully = False
        self.CommandExecutionTime = 0.23  # Часть времени уходит на исполнение команды (отправку частоты на
                                        # частотник, обновление отрисовки). Надо подобрать этот параметр,
                                        # и начинать исполнение команды на dt раньше, чтобы учесть задержку по времени
                                        # на исполнение команды
        self.DebugMode = True



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
        DeltaTimes = SignalData.dx
        N = len(DeltaTimes)

        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 1
        self.TimeStamp = Time[self.PointsIterator - 1]
        self.ValueToSend = SignalData.y[self.PointsIterator]  # Сигнал опережает теперь
        preset_value = SignalData.y[0]

        if self.IsFirstCycle == True:
            # На первом прогоне надо предварительно выставить начальную частоту
            self.IsFirstCycle = False
            self.PresetFrequency(preset_value)

        if self.Timer.if_started == True:  # Если уже дали старт таймеру на предудущем цикле
            self.Timer.reset(DeltaTimes[0] - self.CommandExecutionTime)
        else:
            self.Timer.interval = DeltaTimes[0] - self.CommandExecutionTime
            self.Timer.run()

        if N != 1:  # If the Time array has only one point, then we've already accomplished it in
                    # the method self.Timer.run()
            i = 0
            i_limit = N - 2
            while i < i_limit:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False
                    i += 1
                    self.PointsIterator += 1

                    self.ValueToSend = SignalData.y[self.PointsIterator]
                    self.TimeStamp = Time[self.PointsIterator - 1]

                    self.Timer.reset(DeltaTimes[i-1] - self.CommandExecutionTime)


                if self.SendingStopped:
                    print('Stop push button --> finishing thread execution')
                    return
        while True:  # Дожидаемся отправки последней команды (на краю сэмпла, чтобы на визуализации тоже это увидеть)
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                print(f'Finished CYCLE!')
                return


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

                # restarting points Iterator, Visualisation and Sending Thread
                self.PointsIterator = 0
                self.SignalVisualizer.Restart(Time)
                self.ExecuteSending(Time)

    def Restart(self, Time):
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



    # TODO: Исправить баг, когда StopSignalSending, потом рестарт - не отрисовывается визуализация
    def StartSendingSignal(self):
        if self.SendingThread is None:
            print(f'launching thread')
            if not self.SignalVisualizerConstructed:
                self.SignalVisualizer = SignalVisualizer()
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
        value_to_send = int(self.ValueToSend * 100)  # Привести к инту, иначе pymodbus выдаёт ошибку
        self.DeltaCPClient.SetFrequency(value_to_send)
        CurrentFreq = self.DeltaCPClient.RequestCurrentFrequency()
        self.SignalVisualizer.UpdateSetFrequency(self.TimeStamp, self.ValueToSend)
        self.SignalVisualizer.UpdateCurrentFrequency(self.TimeStamp, CurrentFreq)

        self.FunctionWasCalled = True

    def PresetFrequency(self, value):
        # Перед запуском, если частота ненулевая - убедиться, предварительно задать требуемую начальную частоту
        value_to_send = int(value * 100)  # Привести к инту, иначе pymodbus выдаёт ошибку
        self.DeltaCPClient.SetFrequency(value_to_send)
        accuracy = 0.05

        if self.DebugMode:
            return
        else:
            while True:
                # мониторим, достигли ли требуемой начальной частоты
                sleep(1)
                current_freq = self.DeltaCPClient.RequestCurrentFrequency()
                if abs(current_freq - value_to_send) <= accuracy:
                    return





