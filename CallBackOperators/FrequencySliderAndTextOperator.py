from CallBackOperator import CallBackOperator


class FrequencySliderAndTextOperator(CallBackOperator):
    def __init__(self):
        self.window = None

    def ConnectCallBack(self, window):
        self.window = window


