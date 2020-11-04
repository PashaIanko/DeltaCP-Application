from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters
from DeltaCPClient import DeltaCPClient
import pandas as pd


class AutoConnectOperator(CallBackOperator):
    def __init__(self):
        self.window = None
        self.ConnectionParameters = ConnectionParameters()
        self.DeltaCPClient = DeltaCPClient()
        self.ConnectionConfigs = pd.read_excel(".\\Connection_Configs\\Connection_Configs.xlsx")


    def ConnectCallBack(self, window):
        window.AutoConnectpushButton.clicked.connect(self.AutoConnect)
        self.window = window

    def AutoConnect(self):
        for index, config in self.ConnectionConfigs.iterrows():
            self.set_config_into_comboboxes\
            (
                [config['Protocol'],        self.window.ProtocolcomboBox],
                [str(config['Byte Size']),  self.window.ByteSizecomboBox],
                [config['Parity'],          self.window.ParitycomboBox],
                [str(config['Stop Bits']),  self.window.StopBitscomboBox],
                [config['COM Port'],        self.window.COMPortcomboBox],
                [str(config['Baud Rate']),  self.window.BaudRatecomboBox]
            )

            ConnectionParameters = self.ConnectionParameters.GetConnectionParameters()
            print(f'Auto Connect for config = {ConnectionParameters}')

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
                print(f'Auto Connection successful') # TODO: Вместо print сделать предупредительное pop up окно
                break

        print(f'Auto Connection was not successful. Please write other configs into'
              f' Connection_Configs.xlsx file or set parameters manually')  # TODO: Вместо print сделать предупредительное pop up окно




    def set_config_into_comboboxes(self, *param_combobox_pairs):
        for pair in param_combobox_pairs:
            val = pair[0]
            combo_box = pair[1]
            combo_box_items = [combo_box.itemText(i) for i in range(combo_box.count())]
            if not (val in combo_box_items):
                combo_box.addItems([val])
            combo_box.setCurrentText(val)
