from SignalGenerationPackage.SignalController import SignalController
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleModel import ExperimentScheduleModel
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleObserver import ExperimentScheduleObserver
from SignalGenerationPackage.ExperimentSchedule.ExperimentScheduleMainWindow import ExperimentScheduleMainWindow
from SignalGenerationPackage.ExperimentSchedule.CallBacks.ScheduleAutoFillOperator import ScheduleAutoFillOperator
from CallBackOperators.PIDSendingOperator import PIDSendingOperator
from DebugConfigs import DebugConfigs

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
        self.param_names = [
            'Frequencies',  # Эти параметры передаются на AutoFill Operator, чтобы
            # понять, соответствуют ли параметры в екселе тем, которые мы ожидаем на вход
            'Seconds',
            'Request every N seconds'
        ]

    # overridden
    def init_slider_text_pairs(self):
        self.slider_text_pairs = [
            # Никаких слайдеров не предусмотрено
            # на интерфейсе расписания эксперимента
        ]

    # overridden
    def init_plot_widget(self):
        self.plot_widget = self.main_window.user_interface.plot_widget

    # overridden
    def init_callback_operators(self):
        self.callback_operators = [
            ScheduleAutoFillOperator(self.main_window.user_interface, self.param_names, model=self.model,
                                     configs_folder=".\\SignalGenerationConfigs\\ExperimentScheduleConfigs\\")
            # Путь только до папки, файл открывается по новой, в зависимости от имени файла
            # с расписанием, введённым пользователем
        ]

    # overridden
    def append_sending_operator(self):
        self.callback_operators.append(
            PIDSendingOperator(self.main_window, self.plot_widget, model=self.model, DebugMode=DebugConfigs.PIDOperatorDebug,
                               SendRetry=True
            )
        )