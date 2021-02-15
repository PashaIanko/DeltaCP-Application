from ApplicationModule import ApplicationModule
from CallBackOperators.SetAndStopFrequencyOperator import SetAndStopFrequencyOperator
from CallBackOperators.FrequencySliderAndTextOperator import FrequencySliderAndTextOperator
#from CallBackOperators.FrequencySliderLimitsOperator import FrequencySliderLimitsOperator

class FrequencySettingModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    # overridden
    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                SetAndStopFrequencyOperator(),  # Controlls the "Set Frequency" and "Stop Frequency" buttons
                FrequencySliderAndTextOperator(),  # To connect callbacks from slider and TextField
                #FrequencySliderLimitsOperator()
            ]