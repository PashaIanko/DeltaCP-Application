from CallBackOperator import CallBackOperator
from DeltaCPClient import DeltaCPClient
from DeltaCPRegisters import DeltaCPRegisters
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
        self.client.SendStart()

    def SetFrequency(self):
        lineEditText = self.window.OutputFrequencylineEdit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0.0'

        lineEditText = lineEditText.replace(',', '.')

        try:
            self.client.WriteRegister(DeltaCPRegisters.FrequencyCommandRegister,
                                      float(lineEditText))
        except:
            print(sys.exc_info())




    def SendStopCommand(self):
        self.client.SendStop()

    def RequestCurrentFrequency(self):
        #  Узнать истинную частоту в данный момент времени
        try:
            self.client.ReadRegister(DeltaCPRegisters.CurrentFrequencyRegister)
        except:
            print(sys.exc_info())


    def RequestSetFrequency(self):
        #  Узнать, какую частоту мы задали (Output Frequency Command)
        try:
            self.client.ReadRegister(DeltaCPRegisters.SetFrequencyRegister)
        except:
            print(sys.exc_info())