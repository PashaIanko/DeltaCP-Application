from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters
from DeltaCPClient import DeltaCPClient

class ConnectionOperator(CallBackOperator):
    def __init__(self):
        self.window = None
        # SINGLETON!
        self.ConnectionParameters = ConnectionParameters()
        self.DeltaCPClient = DeltaCPClient()


    def ConnectCallBack(self, window):
        window.ConnectpushButton.clicked.connect(self.Connect)
        self.window = window

    def Connect(self):
        print('in Connect')
        ConnectionParameters = self.ConnectionParameters.GetConnectionParameters()

        try:
            self.DeltaCPClient.CreateClient(
                Protocol=ConnectionParameters['Protocol'],
                COMPort=ConnectionParameters['COMPort'],
                Timeout=ConnectionParameters['Timeout'],
                StopBits=ConnectionParameters['StopBits'],
                ByteSize=ConnectionParameters['ByteSize'],
                Parity=ConnectionParameters['Parity'],
                BaudRate=ConnectionParameters['BaudRate']
            )
        except:
            print('exception')
            return
        if_connected = self.DeltaCPClient.Connect()
        print(if_connected)
