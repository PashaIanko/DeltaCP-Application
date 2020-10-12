from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class TimeToCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.lineEditTimeTo.setValidator(QDoubleValidator(0.00, 6000.00, 2))
        window.lineEditTimeTo.textChanged.connect(self.SetTimeTo)


    def SetTimeTo(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.X_to = float(text)
        except:
            print(sys.exc_info())