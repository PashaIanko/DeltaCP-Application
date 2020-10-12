from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class AccelerationTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.lineEditAccelerationTime.setValidator(QDoubleValidator(0.00, 600.00, 2))
        window.lineEditAccelerationTime.textChanged.connect(self.SetAccelerationTime)


    def SetAccelerationTime(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.AccelerationTime = float(text)
        except:
            print(sys.exc_info())