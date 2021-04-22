from CallBackOperator import CallBackOperator


class FrequencySliderAndTextOperator(CallBackOperator):
    def __init__(self, model=None, value_range=None):
        super().__init__(model, model, value_range)


    # overridden
    def init_slider(self):
        self.slider = self.window.FrequencySetSlider

    # overridden
    def init_line_edit(self):
        self.line_edit = self.window.OutputFrequencylineEdit

    def ConnectCallBack(self):
        self.SynchronizeSliderandText()

    # overridden
    def value_changed(self, val):
        pass

