from CallBackOperator import CallBackOperator
from SignalGenerationPackage.Sinus.SinusSignalController import SinusSignalController
from SignalGenerationPackage.UserSignal.UserSignalController import UserSignalController
from SignalGenerationPackage.DynamicPointsDensitySignal.DynamicPointsDensitySignalController import DynamicPointsDensitySignalController
from SignalGenerationPackage.EdgeSignal.EdgeSignalController import EdgeSignalController

class SignalTypeOperator(CallBackOperator):
    def __init__(self, window, model=None, value_range=None):
        super().__init__(window, model, value_range)



    def ConnectCallBack(self):
        self.window.SignalTypecomboBox.currentIndexChanged.connect(self.StartSignalGeneration)

    def StartSignalGeneration(self):
        signal_text = self.window.SignalTypecomboBox.currentText()
        if signal_text == 'sin':
            self.SignalController = SinusSignalController()
        elif signal_text == 'user signal':
            self.SignalController = UserSignalController()
        elif signal_text == 'dynamic points density':
            self.SignalController = DynamicPointsDensitySignalController()
        elif signal_text == 'edge signal':
            self.SignalController = EdgeSignalController()
        # TODO: убрать ветвление, вставить словарь

    # overridden
    def value_changed(self, val):
        pass

    # overridden
    def init_line_edit(self):
        pass

    # overridden
    def init_slider(self):
        pass