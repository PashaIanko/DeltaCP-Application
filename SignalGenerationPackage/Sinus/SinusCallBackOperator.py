
from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys

class SinusCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        print(sys.exc_info())
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        # window.TestpushButton1.clicked.connect(self.SetAmplitude)

        window.lineEditAmplitude.setValidator(QDoubleValidator(0.99,99.99,2))
        window.lineEditAmplitude.textChanged.connect(self.SetAmplitude)


    def SetAmplitude(self, text):
        print(f'in callbackk {text} {type(text)}')
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.amplitude = float(text)
        except:
            print(sys.exc_info())