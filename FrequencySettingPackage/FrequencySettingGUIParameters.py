
class FrequencySettingGUIParameters:

    FrequencyMin = 0.0
    FrequencyMax = 100.0
    FrequencyLineEditAccuracy = 2  # Number of digits after dot

    FrequencySliderMin = FrequencyMin ** (FrequencyLineEditAccuracy)  # These calculations for correct
                                                                        # scaling of values on the slider
    FrequencySliderMax = FrequencyMax ** (FrequencyLineEditAccuracy)


    def __init__(self):
        pass

