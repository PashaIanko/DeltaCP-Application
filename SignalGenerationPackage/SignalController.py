from abc import ABC, abstractmethod


class SignalController(ABC):

    def __init__(self):
        self.main_window = None
        self.model = None
        self.observer = None
        self.callback_operators = None

        self.param_names = None
        self.slider_constants = None
        self.sliders = None

        self.plot_widget = None  # Окошечко с графиком, где будем отрисовывать

        # Процедура конструктора - надо переопределить все методы
        self.init_model()
        self.init_main_window()
        self.init_observer()

        # Далее, в процедуре конструктора, надо указать лист из слайдеров, нормирующих констант и
        # названий параметров сигнала в excel файлах. Это необходимо для Auto-Fill, и сохранения
        # пресетов
        self.init_param_names()
        self.init_slider_constants()
        self.init_plot_widget()
        self.init_sliders()

        # После этого инициируем операторы, в том числе AutoFillOperator, SavePresetOperator
        # и оператор, который будет заниматься отправкой сигнала
        self.init_callback_operators()
        self.append_sending_operator()
        self.connect_all_callbacks()
        self.show_gui()

    @abstractmethod
    def init_plot_widget(self):
        pass  # Определить, в какой окошке с графиком будет отрисовка отправки сигнала ("Окошечко" - это класс PlotCanvas)

    @abstractmethod
    def append_sending_operator(self):
        pass  # В переопределённом потомком методе определяем - какой CallBackOperator будет ответственнен за
                # Отправку сигнала (NaiveSendingOperator, ForwardSendingOperator)

    @abstractmethod
    def init_param_names(self):
        pass

    @abstractmethod
    def init_slider_constants(self):
        pass

    @abstractmethod
    def init_sliders(self):
        pass

    def connect_all_callbacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack()

    @abstractmethod
    def init_model(self):
        pass

    @abstractmethod
    def init_observer(self):
        pass

    @abstractmethod
    def init_callback_operators(self):
        pass

    @abstractmethod
    def init_main_window(self):
        pass

    def show_gui(self):
        self.main_window.show()