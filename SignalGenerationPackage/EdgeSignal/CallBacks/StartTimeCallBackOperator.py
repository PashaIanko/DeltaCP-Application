from CallBackOperator import CallBackOperator


class StartTimeCallBackOperator(CallBackOperator):

    def __init__(self, window, model, value_range):
        super().__init__(window, model, value_range)


    # overridden
    def init_line_edit(self):
        self.line_edit = self.window.StartTimelineEdit

    # overridden
    def init_slider(self):
        self.slider = self.window.StartTimehorizontalSlider

    # overridden
    def ConnectCallBack(self):
        self.SynchronizeSliderandText()

    # overridden
    def value_changed(self, val):
        self.model.StartTime = val