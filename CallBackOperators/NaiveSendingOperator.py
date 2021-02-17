from SignalGenerationPackage.SignalData import SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator
from LoggersConfig import loggers


class NaiveSendingOperator(SignalSendingOperator):

    # Реализует "Наивную" отправку. На графика сигнала, по оси икс - моменты времени
    # по Y - какое значение сигнала отправить. Т.е. гарантируется, что в этот момент времени
    # Будет отправлено значение на графике. В новой стратегии (ForwardSendingOperator) реализовано
    # Так, чтобы в текущий момент времени мы не задали, а УЖЕ ИМЕЛИ данное значение
    # Как истинную частоту в этот момент времени.

    def __init__(self):
        super().__init__()

    # overridden
    def ExecuteSending(self, Time):
        DeltaTimes = SignalData.dx
        Dts_len = len(DeltaTimes)

        self.FunctionWasCalled = False  # Line is important! For multithreading
        self.PointsIterator = 0
        self.TimeStamp = Time[self.PointsIterator]
        self.ValueToSend = SignalData.y[self.PointsIterator]


        loggers['SignalSending'].info(f'Now t={self.TimeStamp}. After dt={self.CycleGap} will send {self.ValueToSend}')
        if self.Timer.if_started:  # Если уже дали старт таймеру на предудущем цикле
            self.Timer.reset(self.CycleGap)  # Время ожидания перед отправкой (так же перерыв между циклами)
        else:
            self.Timer.interval = self.CycleGap
            self.Timer.run()  # Подождали DeltaTimes[0] и отправили 0ую точку


        # После отправки нулевой точки - увеличиваем итератор
        self.PointsIterator += 1
        if Dts_len != 0:  # If the Time array has only one point, then we've already accomplished it in
                          # the method self.Timer.run()
            i = 0
            while i < Dts_len:
                if self.FunctionWasCalled and not self.SendingOnPause and not self.SendingStopped:
                    self.FunctionWasCalled = False

                    self.ValueToSend = SignalData.y[self.PointsIterator]
                    self.TimeStamp = Time[self.PointsIterator]
                    dt_to_wait = DeltaTimes[i] - self.CommandExecutionTime
                    loggers['SignalSending'].info(
                        f'Now t={self.TimeStamp}. After dt={dt_to_wait} will send {self.ValueToSend}')
                    self.Timer.reset(dt_to_wait)

                    i += 1
                    self.PointsIterator += 1

                if self.SendingStopped:
                    loggers['Application'].info(f'Sending stopped. Finish execution')
                    loggers['Debug'].debug(f'Sending stopped. Finish execution')
                    return

        while True: # Дожидаемся отправки последней команды (на краю сэмпла, чтобы на визуализации тоже это увидеть)
            if self.FunctionWasCalled == True:
                self.FunctionWasCalled = False
                self.CycleFinishedSuccessfully = True
                loggers['SignalSending'].info(f'Finished cycle')
                loggers['Debug'].debug(f'Finished cycle')
                return

    # overridden
    def get_start_button(self):
        return self.user_interface.pushButtonStartSignalSending

    # overridden
    def get_pause_radio_button(self):
        return self.user_interface.PauseSendingradioButton

    # overridden
    def get_resume_radio_button(self):
        return self.user_interface.ResumeSendingradioButton

    # overridden
    def get_stop_button(self):
        return self.user_interface.pushButtonStopSignalSending

    # overridden
    def get_endless_send_checkbox(self):
        return self.user_interface.EndlessSendingcheckBox


















