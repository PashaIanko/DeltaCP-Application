from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import sys


class PlateauTimeCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        self.Model = Model

    # overriden
    def ConnectCallBack(self, window):
        window.PlateauTimelineEdit.setValidator(QDoubleValidator(0.00, 600.00, 2))
        window.PlateauTimelineEdit.textChanged.connect(self.SetPlateauTime)


    def SetPlateauTime(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.PlateauTime = float(text)
        except:
            print(sys.exc_info())