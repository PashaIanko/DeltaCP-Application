from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class EndTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.EndTimelineEdit.setValidator(QDoubleValidator(0.00, 6000.00, 2))
        window.EndTimelineEdit.textChanged.connect(self.SetEndTime)


    def SetEndTime(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.EndTime = float(text)
        except:
            print(sys.exc_info())