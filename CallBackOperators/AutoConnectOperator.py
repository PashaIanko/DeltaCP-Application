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
        print(f'auto connection')

        #print(self.ConnectionConfigs.head())
        #print(self.ConnectionConfigs.shape[0])
        #config_size = self.ConnectionConfigs.shape[0] - 1

        try:
            for index, config in self.ConnectionConfigs.iterrows():
                protocol = config['Protocol']
                byte_size = config['Byte Size']
                parity = config['Parity']
                stop_bits = config['Stop Bits']
                com_port = config['COM Port']
                baud_rate = config['Baud Rate']
                self.set_config_and_connect(protocol, byte_size, parity, stop_bits, com_port, baud_rate)

        except:
            print(sys.exc_info())

    def set_config_and_connect(self, protocol, byte_size, parity, stop_bits, com_port, baud_rate):
        #AllItems = [QComboBoxName.itemText(i) for i in range(QComboBoxName.count())]
        self.window.BaudRatecomboBox.addItems([str(baud_rate)])
        self.window.BaudRatecomboBox.setCurrentText(str(baud_rate))

        #geek_list = ["100", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
        #self.window.BaudRatecomboBox.addItems(geek_list)

        #self.window.BaudRatecomboBox.setCurrentText('1200')
