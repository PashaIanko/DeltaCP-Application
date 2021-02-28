from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from DeltaCPRegisters import DeltaCPRegisters
from LoggersConfig import loggers
import sys


class SetAndStopFrequencyOperator(CallBackOperator):
    def __init__(self):
        self.window = None
        self.client = DeltaCPClient()


    def ConnectCallBack(self, window):
        window.SetFrequencypushButton.clicked.connect(self.SetFrequency)
        window.StartFrequencypushButton.clicked.connect(self.SendStartCommand)
        window.StopFrequencypushButton.clicked.connect(self.SendStopCommand)
        # window.RequestCurrentFrequencypushButton.clicked.connect(self.RequestCurrentFrequency)
        # window.RequestSetFrequencypushButton.clicked.connect(self.RequestSetFrequency)
        self.window = window


    def SendStartCommand(self):
        self.client.SendStart()

    def SetFrequency(self):
        lineEditText = self.window.OutputFrequencylineEdit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0.0'

        lineEditText = lineEditText.replace(',', '.')
        #  Если хотим 10 Гц, то представление частоты (XXX.XX Hz) --> Надо
        #  Отправлять int число == 1000 (Два нуля приписали)
        value_to_send = int(float(lineEditText) * 100)
        try:
            self.client.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister,
                                      value_to_send)
        except:
            loggers['Debug'].debug(f'SetFrequency: {sys.exc_info()}')


    def SendStopCommand(self):
        self.client.SetFrequency(0)
        self.client.SendStop()


    # def RequestCurrentFrequency(self):
    #     #  Узнать истинную частоту в данный момент времени
    #     try:
    #         CurrentFreq = self.client.RequestCurrentFrequency()
    #         loggers['Debug'].debug(f'CurrentFreq = {CurrentFreq}')
    #     except:
    #         loggers['Debug'].debug(f'RequestCurrentFrequency: {sys.exc_info()}')
    #
    #
    # def RequestSetFrequency(self):
    #     #  Узнать, какую частоту мы задали (Output Frequency Command)
    #     try:
    #         SetFreq = self.client.RequestSetFrequency()
    #     except:
    #         loggers['Debug'].debug(f'RequestSetFrequency: {sys.exc_info()}')