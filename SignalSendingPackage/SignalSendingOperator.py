from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from abc import abstractmethod
from SignalSendingPackage.SignalVisualizer import SignalVisualizer
from threading import Thread
from SignalSendingPackage.SignalTimer import SignalTimer
from SignalGenerationPackage.SignalData import SignalData
from LoggersConfig import loggers


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
        self.SignalVisualizerConstructed = False
        self.SendingOnPause = False
        self.SendingStopped = False
        self.EndlessSendingEnabled = False
        self.CycleFinishedSuccessfully = False

        self.SendingThread = None
        self.SignalVisualizer = None
        self.PointsIterator = 0  # Just Counter to iterate over [x, y] arrays of SignalData

        self.CycleGap = 1.0  # Сколько секунд ожидать перед отправкой следующего цикла? (При непрерывной отправке)
        self.CommandExecutionTime = 0.23  # Часть времени уходит на исполнение команды (отправку частоты на
                                            # частотник, обновление отрисовки). Надо подобрать этот параметр,
                                            # и начинать исполнение команды на dt раньше, чтобы учесть задержку по времени
                                            # на исполнение команды


    @abstractmethod
    def ExecuteSending(self, Time):
        pass

    # overridden
    def ConnectCallBack(self, window):
        self.window = window
        window.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)
        window.PauseSendingradioButton.toggled.connect(self.PauseSending)
        window.ResumeSendingradioButton.toggled.connect(self.ResumeSending)
        window.pushButtonStopSignalSending.clicked.connect(self.StopSendingSignal)
        window.EndlessSendingcheckBox.stateChanged.connect(lambda: self.EnableEndlessSending())

    # TODO: на нажатие кнопки Stop Signal Sending надо сделать реакцию - закрытие окошка визуализации

    def EnableEndlessSending(self):
        self.EndlessSendingEnabled = \
            self.window.EndlessSendingcheckBox.isChecked()

    def PauseSending(self):
        if self.window.PauseSendingradioButton.isChecked():
            loggers['Application'].info('Sending Paused')
            loggers['SignalSending'].info('Sending Paused')

            self.SendingOnPause = True
            self.window.ResumeSendingradioButton.setChecked(False)
        else:
            self.window.ResumeSendingradioButton.setChecked(True)

    def ResumeSending(self):
        if self.window.ResumeSendingradioButton.isChecked():
            loggers['Application'].info('Sending Paused')
            loggers['SignalSending'].info('Sending Paused')

            self.SendingOnPause = False
            self.window.PauseSendingradioButton.setChecked(False)
        else:
            self.window.PauseSendingradioButton.setChecked(True)

    def StopSendingSignal(self):
        self.DeltaCPClient.SetFrequency(0.0)
        self.DeltaCPClient.SendStop()
        self.SendingStopped = True

        loggers['Debug'].debug(f'Stopping sending thread')
        if not (self.SendingThread is None):
            self.SendingThread.join()
            self.SendingThread = None
        # # TODO: Исправить баг, когда StopSignalSending, потом рестарт - не отрисовывается визуализация

    def TestTimer(self):
        # Перед отправкой частоты по прерыванию, необходимо проверить - а не закрыл ли пользователь
        # окошко с визуализацией. Если закрыл - то мы ничего уже не отправляем. Тогда выставляем частоту 0Гц
        # SetFrequency(0) и посылаем STOP

        window_is_closed = self.SignalVisualizer.check_if_window_closed()
        if window_is_closed:
            loggers['Application'].info(f'Visualization window was closed --> Application Stop Signal Sending')
            self.StopSendingSignal()
        else:
            # Если окошко не закрыто - продолжаем визуализацию и отправку
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


    # TODO: Исправить баг, когда StopSignalSending, потом рестарт - не отрисовывается визуализация
    def StartSendingSignal(self):
        if self.SendingThread is None:
            loggers['Debug'].debug(f'Launching thread')
            if not self.SignalVisualizerConstructed:
                self.SignalVisualizer = SignalVisualizer()
            self.DeltaCPClient.SendStart()
            self.LaunchSendingThread()
        else:
            if not self.SendingThread.is_alive():
                loggers['Debug'].debug(f'Launching thread')
                self.SignalVisualizer.Restart(TimeArray=[])
                self.RestartSignalIterator()
                self.SendingStopped = False  # Надо почистить этот флаг
                self.LaunchSendingThread()
            else:
                loggers['Debug'].debug(f'Prev sending thread is executing, cant launch one')

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
                    Time[i] += upd_val  # + SignalData.dx[i]

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




