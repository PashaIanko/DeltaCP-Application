from CallBackOperator import CallBackOperator


class AccelerationTimeCallBackOperator(CallBackOperator):

    def __init__(self, window, model, value_range):
        super().__init__(window, model, value_range)


    # overridden
    def init_line_edit(self):
        self.line_edit = self.window.AccelerationTimelineEdit

    # overridden
    def init_slider(self):
        self.slider = self.window.AccelerationTimehorizontalSlider

    # overridden
    def ConnectCallBack(self):
        self.SynchronizeSliderandText()

    # overridden
    def value_changed(self, val):
        self.model.AccelerationTime = val