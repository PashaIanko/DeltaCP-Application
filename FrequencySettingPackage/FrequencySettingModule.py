from ApplicationModule import ApplicationModule
from CallBackOperators.SetAndStopFrequencyOperator import SetAndStopFrequencyOperator
from CallBackOperators.FrequencySliderAndTextOperator import FrequencySliderAndTextOperator

class FrequencySettingModule(ApplicationModule):

    callback_operators = \
        [
            SetAndStopFrequencyOperator(),  # Controlls the "Set Frequency" and "Stop Frequency" buttons
            FrequencySliderAndTextOperator()  # To connect callbacks from slider and TextField
        ]

    def __init__(self):
        self.window = None



    def Run(self, MainWindow):
        self.UserInterface = MainWindow.ui
        self.MainWindow = MainWindow
        self.ConnectAllCallBacks()  # TODO: Перенести этот код в родителя


    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.UserInterface)  # TODO: код в родителя

