from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QIntValidator
import sys


class SinusPointsNumberCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        print(sys.exc_info())
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        # window.TestpushButton1.clicked.connect(self.SetAmplitude)
        window.lineEditPointsNumber.setValidator(QIntValidator(0, 500))
        window.lineEditPointsNumber.textChanged.connect(self.SetPointsNumber)


    def SetPointsNumber(self, text):
        print(f'in callbackk {text} {type(text)}')
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.PointsNumber = float(text)
        except:
            print(sys.exc_info())