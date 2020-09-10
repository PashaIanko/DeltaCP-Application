from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QDoubleValidator
import numpy as np
import sys


class SinusPhaseCallBackOperator(CallBackOperator):

    def __init__(self, Model):
        super().__init__()
        print(sys.exc_info())
        self.Model = Model
        self.PhaseFrom = 0.0
        self.PhaseTo = 2 * np.pi

    # overriden
    def ConnectCallBack(self, window):
        # window.TestpushButton1.clicked.connect(self.SetAmplitude)
        window.lineEditPhase.setValidator(QDoubleValidator(self.PhaseFrom, self.PhaseTo, 2))
        window.lineEditPhase.textChanged.connect(self.SetPhase)


    def SetPhase(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                self.Model.phase = float(text)
        except:
            print(sys.exc_info())