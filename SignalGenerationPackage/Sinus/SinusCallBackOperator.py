
from CallBackOperator import CallBackOperator
import sys

class SinusCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        print(sys.exc_info())
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.TestpushButton1.clicked.connect(self.SetAmplitude)

    def SetAmplitude(self):
        print('in callbackk')
        self.Model.amplitude = 1
