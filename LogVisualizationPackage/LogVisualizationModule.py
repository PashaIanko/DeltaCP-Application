from ApplicationModule import ApplicationModule
from LogVisualizationPackage.CallBackOperator.VisualizationOperator import VisualizationOperator
from DebugConfigs import DebugConfigs

class LogVisualizationModule(ApplicationModule):

    def __init__(self):
        super().__init__()

    # overridden
    def InitCallBackOperators(self, user_interface):
        self.CallBackOperators = \
            [
                VisualizationOperator(user_interface, DebugMode=DebugConfigs.VisualizationOperatorDebug)
            ]