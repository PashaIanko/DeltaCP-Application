from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class SinusTimeFromCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        print(sys.exc_info())
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        # window.TestpushButton1.clicked.connect(self.SetAmplitude)
        window.lineEditTimeFrom.setValidator(QDoubleValidator(0.00, 600.00,2))
        window.lineEditTimeFrom.textChanged.connect(self.SetTimeFrom)


    def SetTimeFrom(self, text):
        print(f'in callbackk {text} {type(text)}')
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.X_from = float(text)
        except:
            print(sys.exc_info())