from CallBackOperator import CallBackOperator


class HighLevelFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, window, model, value_range):
        super().__init__(window, model, value_range)

    # overridden
    def init_line_edit(self):
        self.line_edit = self.window.HighLevelFrequencylineEdit

    # overridden
    def init_slider(self):
        self.slider = self.window.HighLevelFrequencyhorizontalSlider

    # overridden
    def ConnectCallBack(self):
        self.SynchronizeSliderandText()

    # overridden
    def value_changed(self, val):
        self.model.HighLevelFrequency = val