from abc import ABC, abstractmethod


class SignalController(ABC):

    def __init__(self):
        self.main_window = None
        self.model = None
        self.observer = None
        self.callback_operators = None

        # Процедура конструктора - надо переопределить все методы
        self.init_model()
        self.init_main_window()
        self.init_observer()
        self.init_callback_operators()
        self.connect_all_callbacks()
        self.show_gui()



    def connect_all_callbacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.main_window)

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