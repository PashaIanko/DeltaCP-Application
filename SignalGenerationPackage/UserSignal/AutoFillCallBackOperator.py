from CallBackOperator import CallBackOperator
from PyQt5.QtWidgets import QFileDialog, QWidget
import pandas as pd

class AutoFillCallBackOperator(CallBackOperator):
    def __init__(self):
        super().__init__()
        self.configs_path = ".\\SignalGenerationConfigs\\UserSignalConfigs"
        self.configs_data = None

    def ConnectCallBack(self, window):
        self.window = window
        window.AutoFillpushButton.clicked.connect(self.AutoFill)


    def AutoFill(self):
        #filename = self.window.ConfigFileNamelineEdit.text()
        try:
            q = QWidget()
            fileName = QFileDialog.getOpenFileName(q, "Open Signal Config Excel File", self.configs_path, "Files (*.xlsx)")[0]
            print(f'filename is {fileName}')
            self.configs_data = pd.read_excel(f'{fileName}')
            print(self.configs_data.head())

        except:
            import sys
            print(sys.exc_info())


