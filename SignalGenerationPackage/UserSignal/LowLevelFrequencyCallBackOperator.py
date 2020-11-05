from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class LowLevelFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.LowLevelFrequencylineEdit.setValidator(QDoubleValidator(0.00, 600.00, 2))
        window.LowLevelFrequencylineEdit.textChanged.connect(self.SetLowLevelFrequency)


    def SetLowLevelFrequency(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.LowLevelFrequency = float(text)
        except:
            print(sys.exc_info())