from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters
from DeltaCPClient import DeltaCPClient
from LoggersConfig import loggers

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
        already_connected = self.DeltaCPClient.if_connected
        if already_connected:
            print(f'Client is already connected!')  # TODO: Pop Up window here
            return

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
            repr(self.DeltaCPClient)
        except:
            loggers['Debug'].debug(f'Exception while creating DeltaCP Client')
            return
        if_connected = self.DeltaCPClient.Connect()
        loggers['Debug'].debug(f'If client connected: {if_connected}')

        # TODO: Есть Баг - Жмёшь Connect, считываешь частоту, ещё раз жмёшь Connect (уже False). Ещё раз считываешь /
        # частоту - exception (failed to connect)
        #
