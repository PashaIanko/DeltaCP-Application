from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class HighLevelFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.HighLevelFrequencylineEdit.setValidator(QDoubleValidator(0.00, 600.00, 2))
        window.HighLevelFrequencylineEdit.textChanged.connect(self.SetHighLevelFrequency)


    def SetHighLevelFrequency(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.HighLevelFrequency = float(text)
        except:
            print(sys.exc_info())