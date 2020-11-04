from CallBackOperator import CallBackOperator
from ConnectionPackage.ConnectionParameters import ConnectionParameters
from DeltaCPClient import DeltaCPClient
import pandas as pd
import sys


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
            self.set_config_and_connect\
            (
                [config['Protocol'],        self.window.ProtocolcomboBox],
                [str(config['Byte Size']),  self.window.ByteSizecomboBox],
                [config['Parity'],          self.window.ParitycomboBox],
                [str(config['Stop Bits']),  self.window.StopBitscomboBox],
                [config['COM Port'],        self.window.COMPortcomboBox],
                [str(config['Baud Rate']),  self.window.BaudRatecomboBox]
            )


    def set_config_and_connect(self, *param_combobox_pairs):

        for pair in param_combobox_pairs:
            val = pair[0]
            combo_box = pair[1]
            combo_box_items = [combo_box.itemText(i) for i in range(combo_box.count())]
            if not (val in combo_box_items):
                combo_box.addItems([val])
            combo_box.setCurrentText(val)

