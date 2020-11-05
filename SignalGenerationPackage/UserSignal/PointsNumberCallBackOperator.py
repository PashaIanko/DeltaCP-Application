from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QIntValidator
import sys


class PointsNumberCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.PointsNumberlineEdit.setValidator(QIntValidator(0, 500))
        window.PointsNumberlineEdit.textChanged.connect(self.SetPointsNumber)


    def SetPointsNumber(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.PointsNumber = int(text)
        except:
            print(sys.exc_info())