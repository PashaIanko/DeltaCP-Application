from CallBackOperator import CallBackOperator


class RequestFrequencyCallBackOperator(CallBackOperator):

    def __init__(self, main_window, model, value_range):
        super().__init__(window=main_window, model=model, value_range=value_range)

    def ConnectCallBack(self):
        self.SynchronizeSliderandText()

    # overridden
    def init_slider(self):
        self.slider = self.window.RequestFrequencyhorizontalSlider

    # overridden
    def init_line_edit(self):
        self.line_edit = self.window.RequestFrequencylineEdit

    # overridden
    def value_changed(self, val):
        self.model.request_freq = val