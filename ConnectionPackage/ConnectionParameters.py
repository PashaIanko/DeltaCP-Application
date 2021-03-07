from Singleton import Singleton

@Singleton
class ConnectionParameters:
    def __init__(self):
        self.COMPort = 1
        self.BaudRate = 0
        self.Protocol = ""
        self.ByteSize = 0
        self.Parity = ""
        self.StopBits = 0
        self.Timeout = 0.1

    def SetProtocol(self, Protocol):
        self.Protocol = Protocol

    def SetParity(self, Parity):
        self.Parity = Parity

    def SetByteSize(self, ByteSize):
        self.ByteSize = ByteSize

    def SetStopBits(self, StopBits):
        self.StopBits = StopBits

    def SetBaudRate(self, BaudRate):
        self.BaudRate = BaudRate

    def SetCOMPort(self, COMPort):
        self.COMPort = COMPort

    def GetConnectionParameters(self):
        Dict = \
            dict(
                {
                    'Protocol': self.Protocol,
                    'COMPort': self.COMPort,
                    'StopBits': self.StopBits,
                    'ByteSize': self.ByteSize,
                    'Parity': self.Parity,
                    'BaudRate': self.BaudRate,
                    'Timeout': self.Timeout
                }
            )
        return Dict
