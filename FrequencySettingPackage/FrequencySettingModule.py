from ApplicationModule import ApplicationModule
from CallBackOperators.SetAndStopFrequencyOperator import SetAndStopFrequencyOperator
from CallBackOperators.FrequencySliderAndTextOperator import FrequencySliderAndTextOperator
from Ranges import Ranges

class FrequencySettingModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    # overridden
    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                SetAndStopFrequencyOperator(),  # Controlls the "Set Frequency" and "Stop Frequency" buttons
                FrequencySliderAndTextOperator(ValueRange=Ranges.frequency_range),  # To connect callbacks from slider and TextField
                #FrequencySliderLimitsOperator()
            ]