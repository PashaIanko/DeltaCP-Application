from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters

class ComboBoxOperator(CallBackOperator):

    def __init__(self, window, model=None, value_range=None):
        super().__init__(window, model, value_range)
        self.ConnectionParameters = ConnectionParameters()

    def ConnectCallBack(self):
        self.window.BaudRatecomboBox.currentIndexChanged.connect(self.SetBaudRate)
        self.window.COMPortspinBox.valueChanged.connect(self.SetCOMPort)
        self.window.ProtocolcomboBox.currentIndexChanged.connect(self.SetProtocol)
        self.window.ByteSizecomboBox.currentIndexChanged.connect(self.SetByteSize)
        self.window.ParitycomboBox.currentIndexChanged.connect(self.SetParity)
        self.window.StopBitscomboBox.currentIndexChanged.connect(self.SetStopBits)

    # overridden
    def init_line_edit(self):
        pass

    # overridden
    def init_slider(self):
        pass

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

    def value_changed(self, val):
        pass

