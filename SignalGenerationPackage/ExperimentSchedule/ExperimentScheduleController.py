from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleModel import ExperimentScheduleModel
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleObserver import ExperimentScheduleObserver
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleMainWindow import ExperimentScheduleMainWindow

class ExperimentScheduleController(SignalController):
    def __init__(self):
        super().__init__()

    # overridden
    def init_model(self):
        self.model = ExperimentScheduleModel()

    # overridden
    def init_observer(self):
        self.observer = ExperimentScheduleObserver(self.model, self.main_window.plot)

    # overridden
    def init_main_window(self):
        self.main_window = ExperimentScheduleMainWindow()

    # overridden
    def init_param_names(self):
        pass

    # overridden
    def init_slider_text_pairs(self):
        pass

    # overridden
    def init_plot_widget(self):
        pass

    # overridden
    def init_callback_operators(self):
        pass

    # overridden
    def append_sending_operator(self):
        pass