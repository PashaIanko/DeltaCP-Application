from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class VerticalOffsetCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.lineEditVerticalOffset.setValidator(QDoubleValidator(0, 50))
        window.lineEditVerticalOffset.textChanged.connect(self.SetVerticalOffset)


    def SetVerticalOffset(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.VerticalOffset = float(text)
        except:
            print(sys.exc_info())