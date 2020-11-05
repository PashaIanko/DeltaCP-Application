from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class StartTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.StartTimelineEdit.setValidator(QDoubleValidator(0.00, 6000.00, 2))
        window.StartTimelineEdit.textChanged.connect(self.SetStartTime)


    def SetStartTime(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.StartTime = float(text)
        except:
            print(sys.exc_info())