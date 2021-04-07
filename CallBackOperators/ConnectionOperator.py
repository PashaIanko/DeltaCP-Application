from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters
from DeltaCPClient import DeltaCPClient
from LoggersConfig import loggers
from PopUpNotifier.PopUpNotifier import PopUpNotifier

class ConnectionOperator(CallBackOperator):
    def __init__(self):
        self.window = None

        # Singletons:
        self.ConnectionParameters = ConnectionParameters()
        self.DeltaCPClient = DeltaCPClient()


    def ConnectCallBack(self, window):
        window.ConnectpushButton.clicked.connect(self.Connect)
        self.window = window

    def Connect(self):
        already_connected = self.DeltaCPClient.if_connected
        if already_connected:
            PopUpNotifier.Info(f'Client is already connected!')
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
        except:
            loggers['Debug'].debug(f'Exception while creating DeltaCP Client')
            return
        if_connected = self.DeltaCPClient.Connect()
        self.notify_connection_success(if_connected)
        loggers['Application'].info(f'Connection successful? {if_connected}')
        loggers['Debug'].debug(f'If client connected: {if_connected}')

        # TODO: Есть Баг - Жмёшь Connect, считываешь частоту, ещё раз жмёшь Connect (уже False). Ещё раз считываешь /
        # частоту - exception (failed to connect)
        #

    def notify_connection_success(self, if_connected):
        if if_connected:
            PopUpNotifier.Info(f'Client connection successful!')
        else:
            PopUpNotifier.Error(f'Client connection failed!')

    def value_changed(self, val):
        pass