from ApplicationModule import ApplicationModule
from LogVisualizationPackage.CallBackOperator.VisualizationOperator import VisualizationOperator


class LogVisualizationModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    # overridden
    def InitCallBackOperators(self):
        self.CallBackOperators = \
            [
                VisualizationOperator(DebugMode=True)
            ]