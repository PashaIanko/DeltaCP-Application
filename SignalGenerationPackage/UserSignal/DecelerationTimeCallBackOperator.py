from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class DecelerationTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.lineEditDecelerationTime.setValidator(QDoubleValidator(0.00, 600.00, 2))
        window.lineEditDecelerationTime.textChanged.connect(self.SetDecelerationTime)


    def SetDecelerationTime(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.DecelerationTime = float(text)
        except:
            print(sys.exc_info())