from CallBackOperator import CallBackOperator
from SignalSendingPackage.SignalTimer import SignalTimer
from DeltaCPClient import DeltaCPClient
from abc import abstractmethod
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from threading import Thread


class SignalSendingOperator(CallBackOperator):
    def __init__(self):
        super().__init__()


        # Ниже - Набор параметров для обоих способов отправки сигнала -
        # наперёд (Как Сергей сказал), и более наивный способ
        self.TimeStamp = 0
        self.ValueToSend = 0
        self.Timer = SignalTimer(interval=1.0, function=self.TestTimer)
        self.DeltaCPClient = DeltaCPClient()
        self.FunctionWasCalled = False
        self.SendingThreadWasLaunched = False
        self.SendingThread = None

        self.SignalVisualizer = None
        self.SignalVisualizerConstructed = False

        self.PointsIterator = 0  # Just Counter to iterate over [x, y] arrays of SignalData
        self.SendingOnPause = False
        self.SendingStopped = False
        self.EndlessSendingEnabled = False
        self.CycleFinishedSuccessfully = False
        self.CommandExecutionTime = 0.23  # Часть времени уходит на исполнение команды (отправку частоты на
                                            # частотник, обновление отрисовки). Надо подобрать этот параметр,
                                            # и начинать исполнение команды на dt раньше, чтобы учесть задержку по времени
                                            # на исполнение команды



    @abstractmethod
    def ConnectCallBack(self, window):
        self.window = window
        window.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)
        window.PauseSendingradioButton.toggled.connect(self.PauseSending)
        window.ResumeSendingradioButton.toggled.connect(self.ResumeSending)
        window.pushButtonStopSignalSending.clicked.connect(self.StopSendingSignal)
        window.EndlessSendingcheckBox.stateChanged.connect(lambda: self.EnableEndlessSending())


    def EnableEndlessSending(self):
        self.EndlessSendingEnabled = \
            self.window.EndlessSendingcheckBox.isChecked()

    def PauseSending(self):
        if self.window.PauseSendingradioButton.isChecked():
            print('Paused')
            self.SendingOnPause = True
            self.window.ResumeSendingradioButton.setChecked(False)
        else:
            self.window.ResumeSendingradioButton.setChecked(True)

    def ResumeSending(self):
        if self.window.ResumeSendingradioButton.isChecked():
            print('Resumed')
            self.SendingOnPause = False
            self.window.PauseSendingradioButton.setChecked(False)
        else:
            self.window.PauseSendingradioButton.setChecked(True)

    def StopSendingSignal(self):
        self.DeltaCPClient.SetFrequency(0.0)
        self.DeltaCPClient.SendStop()
        self.SendingStopped = True

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


    def TestTimer(self):
        value_to_send = int(self.ValueToSend * 100)  # Привести к инту, иначе pymodbus выдаёт ошибку
        self.DeltaCPClient.SetFrequency(value_to_send)
        CurrentFreq = self.DeltaCPClient.RequestCurrentFrequency()
        self.SignalVisualizer.UpdateSetFrequency(self.TimeStamp, self.ValueToSend)
        self.SignalVisualizer.UpdateCurrentFrequency(self.TimeStamp, CurrentFreq)
        self.FunctionWasCalled = True

    def RestartSignalIterator(self):
        self.PointsIterator = 0

    def RestartVisualization(self, TimeArray):
        print(f'Restarting Visualization!!')
        self.SignalVisualizer.Restart(TimeArray)

    def LaunchSendingThread(self):
        self.SendingThread = Thread(target=self.ThreadFunc)
        self.SendingThread.start()




