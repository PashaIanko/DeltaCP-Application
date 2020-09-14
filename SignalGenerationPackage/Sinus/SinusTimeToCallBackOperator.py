from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class SinusTimeToCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        print(sys.exc_info())
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        # window.TestpushButton1.clicked.connect(self.SetAmplitude)
        window.lineEditTimeTo.setValidator(QDoubleValidator(10.00, 1200.00,2))
        window.lineEditTimeTo.textChanged.connect(self.SetTimeTo)


    def SetTimeTo(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.X_to = float(text)
        except:
            print(sys.exc_info())