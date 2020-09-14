from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import numpy as np
import sys


class SinusOmegaCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        print(sys.exc_info())
        self.Model = Model
        self.OmegaFrom = 0.0
        self.OmegaTo = 100.0

    # overriden
    def ConnectCallBack(self, window):
        # window.TestpushButton1.clicked.connect(self.SetAmplitude)
        window.lineEditOmega.setValidator(QDoubleValidator(self.OmegaFrom, self.OmegaTo, 2))
        window.lineEditOmega.textChanged.connect(self.SetOmega)


    def SetOmega(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.omega = float(text)
        except:
            print(sys.exc_info())