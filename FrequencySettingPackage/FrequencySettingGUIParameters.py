
class FrequencySettingGUIParameters:

    FrequencyMin = 0.0
    FrequencyMax = 50.0
    FrequencyLineEditAccuracy = 2  # Number of digits after dot

    FrequencyCalcConstant = 100
    FrequencySliderMin = FrequencyMin * FrequencyCalcConstant
    FrequencySliderMax = FrequencyMax * FrequencyCalcConstant


    def __init__(self):
        pass

