from CallBackOperator import CallBackOperator
from PyQt5.QtGui import QIntValidator
from FrequencySettingPackage.FrequencySettingGUIParameters import FrequencySettingGUIParameters
import sys


class FrequencySliderLimitsOperator(CallBackOperator):
    def __init__(self):
        self.window = None

    def ConnectCallBack(self, window):
        self.window = window

        window.FrequencyMinlineEdit.setValidator(QIntValidator())
        window.FrequencyMaxlineEdit.setValidator(QIntValidator())

        window.FrequencyMinlineEdit.textChanged.connect(self.SetFrequencyMin)
        window.FrequencyMaxlineEdit.textChanged.connect(self.SetFrequencyMax)


    def SetFrequencyMin(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                FrequencySettingGUIParameters.FrequencySliderMin = float(text)
        except:
            print(sys.exc_info())


    def SetFrequencyMax(self, text):
        try:
            if(type(text) is str):
                text = text.replace(',', '.')
                FrequencySettingGUIParameters.FrequencySliderMax = float(text)
        except:
            print(sys.exc_info())







