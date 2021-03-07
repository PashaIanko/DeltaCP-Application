from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters

class ComboBoxOperator(CallBackOperator):

    def __init__(self):
        self.window = None
        self.ConnectionParameters = ConnectionParameters()

    def ConnectCallBack(self, window):
        window.BaudRatecomboBox.currentIndexChanged.connect(self.SetBaudRate)
        window.COMPortspinBox.valueChanged.connect(self.SetCOMPort)
        window.ProtocolcomboBox.currentIndexChanged.connect(self.SetProtocol)
        window.ByteSizecomboBox.currentIndexChanged.connect(self.SetByteSize)
        window.ParitycomboBox.currentIndexChanged.connect(self.SetParity)
        window.StopBitscomboBox.currentIndexChanged.connect(self.SetStopBits)
        self.window = window


    def SetProtocol(self):
        arg = self.window.ProtocolcomboBox.currentText()
        if (len(arg)):
            self.ConnectionParameters.SetProtocol(arg)

    def SetByteSize(self):
        arg = (self.window.ByteSizecomboBox.currentText())
        if (len(arg)):
            self.ConnectionParameters.SetByteSize(int(arg))


    def SetParity(self):
        arg = self.window.ParitycomboBox.currentText()
        if (len(arg)):
            self.ConnectionParameters.SetParity(arg)

    def SetStopBits(self):
        arg = (self.window.StopBitscomboBox.currentText())
        if (len(arg)):
            self.ConnectionParameters.SetStopBits(int(arg))

    def SetBaudRate(self):
        arg = (self.window.BaudRatecomboBox.currentText())
        if (len(arg)):
            self.ConnectionParameters.SetBaudRate(int(arg))

    def SetCOMPort(self):
        arg = self.window.COMPortspinBox.value()
        self.ConnectionParameters.SetCOMPort(arg)

