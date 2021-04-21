from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from DeltaCPRegisters import DeltaCPRegisters
from LoggersConfig import loggers
from time import time
import sys


class SetAndStopFrequencyOperator(CallBackOperator):
    def __init__(self, window, model=None, value_range=None):
        super().__init__(window, model, value_range)
        self.client = DeltaCPClient()


    def ConnectCallBack(self):
        self.window.SetFrequencypushButton.clicked.connect(self.SetFrequency)
        self.window.StartFrequencypushButton.clicked.connect(self.SendStartCommand)
        self.window.StopFrequencypushButton.clicked.connect(self.SendStopCommand)

    def SendStartCommand(self):
        self.client.SendStart()

    def SetFrequency(self):
        lineEditText = self.line_edit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0.0'

        lineEditText = lineEditText.replace(',', '.')
        #  Если хотим 10 Гц, то представление частоты (XXX.XX Hz) --> Надо
        #  Отправлять int число == 1000 (Два нуля приписали)
        value_to_send = int(float(lineEditText) * 100)
        try:
            # t1 = time()
            self.client.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister,
                                      value_to_send)
            # t2 = time()
        except:
            loggers['Debug'].debug(f'SetFrequency: {sys.exc_info()}')


    def SendStopCommand(self):
        self.client.SetFrequency(0)
        self.slider.setValue(0)
        self.client.SendStop()


    # overridden
    def init_line_edit(self):
        self.line_edit = self.window.OutputFrequencylineEdit

    # overridden
    def init_slider(self):
        self.slider = self.window.FrequencySetSlider

    # overridden
    def value_changed(self, val):
        pass

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