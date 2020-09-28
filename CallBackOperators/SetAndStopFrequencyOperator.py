from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from DeltaCPRegisters import DeltaCPRegisters
import time
import sys


class SetAndStopFrequencyOperator(CallBackOperator):
    def __init__(self):
        self.window = None
        self.client = DeltaCPClient()

    def ConnectCallBack(self, window):
        window.SetFrequencypushButton.clicked.connect(self.SetFrequency)
        window.StartFrequencypushButton.clicked.connect(self.SendStartCommand)
        window.StopFrequencypushButton.clicked.connect(self.SendStopCommand)
        window.RequestCurrentFrequencypushButton.clicked.connect(self.RequestCurrentFrequency)
        window.RequestSetFrequencypushButton.clicked.connect(self.RequestSetFrequency)
        self.window = window


    def SendStartCommand(self):
        print(f'before sending START command, time={time.asctime()}')
        self.client.SendStart()
        print(f'after sending START command, time={time.asctime()}')

    def SetFrequency(self):
        lineEditText = self.window.OutputFrequencylineEdit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0.0'

        lineEditText = lineEditText.replace(',', '.')
        #  Если хотим 10 Гц, то представление частоты (XXX.XX Hz) --> Надо
        #  Отправлять int число == 1000 (Два нуля приписали)
        value_to_send = int(float(lineEditText) * 100)
        try:
            print('before writing into the register', time.asctime())
            self.client.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister,
                                      value_to_send)
            print('after writing into the register', time.asctime())
        except:
            print(sys.exc_info())




    def SendStopCommand(self):
        print(f'before sending STOP command, time={time.asctime()}')
        self.client.SendStop()
        print(f'after sending STOP command, time={time.asctime()}')

    def RequestCurrentFrequency(self):
        #  Узнать истинную частоту в данный момент времени
        try:
            CurrentFreq = self.client.ReadRegister(DeltaCPRegisters.CurrentFrequencyRegister)
            print('Истинная выходная частота = ', CurrentFreq)
        except:
            print(sys.exc_info())


    def RequestSetFrequency(self):
        #  Узнать, какую частоту мы задали (Output Frequency Command)
        try:
            SetFreq = self.client.ReadRegister(DeltaCPRegisters.SetFrequencyRegister)
            print(f'Заданная частота = {SetFreq}')
        except:
            print(sys.exc_info())