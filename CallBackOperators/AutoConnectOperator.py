from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters
from DeltaCPClient import DeltaCPClient
from LoggersConfig import loggers
from PopUpNotifier.PopUpNotifier import PopUpNotifier
import pandas as pd



class AutoConnectOperator(CallBackOperator):
    def __init__(self, window, model=None, value_range=None):
        super().__init__(window, model, value_range)
        self.ConnectionParameters = ConnectionParameters()
        self.DeltaCPClient = DeltaCPClient()
        self.ConnectionConfigs = pd.read_excel(".\\Connection_Configs\\Connection_Configs.xlsx")

    # overridden
    def ConnectCallBack(self):
        self.window.AutoConnectpushButton.clicked.connect(self.AutoConnect)

    def AutoConnect(self):
        already_connected = self.DeltaCPClient.if_connected
        if already_connected:
            PopUpNotifier.Info('Client already connected!')
            return

        for index, config in self.ConnectionConfigs.iterrows():
            self.set_config_into_comboboxes\
            (
                [config['Protocol'],        self.window.ProtocolcomboBox],
                [str(config['Byte Size']),  self.window.ByteSizecomboBox],
                [config['Parity'],          self.window.ParitycomboBox],
                [str(config['Stop Bits']),  self.window.StopBitscomboBox],
                [str(config['Baud Rate']),  self.window.BaudRatecomboBox]
            )

            ConnectionParameters = self.ConnectionParameters.GetConnectionParameters()

            self.DeltaCPClient.CreateClient(
                Protocol=ConnectionParameters['Protocol'],
                COMPort=ConnectionParameters['COMPort'],
                Timeout=ConnectionParameters['Timeout'],
                StopBits=ConnectionParameters['StopBits'],
                ByteSize=ConnectionParameters['ByteSize'],
                Parity=ConnectionParameters['Parity'],
                BaudRate=ConnectionParameters['BaudRate']
            )

            if_connected = self.DeltaCPClient.Connect()
            if if_connected:
                msg_success = 'Auto connection successful!'
                loggers['Application'].info(msg_success)
                PopUpNotifier.Info(msg_success)
                return

        msg = f'Auto Connect unsuccessful. Please write other configs into Connection_Configs.xlsx' \
              f' file or set parameters manually'
        loggers['Application'].info(msg)
        PopUpNotifier.Warning(msg)

    def set_config_into_comboboxes(self, *param_combobox_pairs):
        for pair in param_combobox_pairs:
            val = pair[0]
            combo_box = pair[1]
            combo_box_items = [combo_box.itemText(i) for i in range(combo_box.count())]
            if not (val in combo_box_items):
                combo_box.addItems([val])
            combo_box.setCurrentText(val)

    # overridden
    def value_changed(self, val):
        pass

    # overridden
    def init_slider(self):
        pass

    # overridden
    def init_line_edit(self):
        pass

