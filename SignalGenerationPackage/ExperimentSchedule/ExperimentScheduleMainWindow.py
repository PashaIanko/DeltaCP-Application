from SignalGenerationPackage.SignalMainWindow import SignalMainWindow
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleWindow import Ui_ExperimentScheduleWindow

class ExperimentScheduleMainWindow(SignalMainWindow):
    def __init__(self):
        super().__init__()

    # overridden
    def init_user_interface(self):
        self.user_interface = Ui_ExperimentScheduleWindow()

    # overridden
    def init_plot(self):
        self.plot = self.user_interface.plot_widget