from CallBackOperator import CallBackOperator


class VisualizationOperator(CallBackOperator):
    def __init__(self):
        self.UserInterface = None



    def ConnectCallBack(self, UserInterface):
        UserInterface.VisualizeLogpushButton.clicked.connect(self.VisualizeLog)
        self.UserInterface = UserInterface

    def VisualizeLog(self):
        print(f'VIZZZ')
