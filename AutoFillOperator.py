from abc import ABC, abstractmethod
import pandas as pd
import sys
from LoggersConfig import loggers

class AutoFillOperator(ABC):
    def __init__(self, model, configs_path):
        super().__init__()
        self.model = model
        self.configs_path = configs_path
        self.configs_data = pd.read_excel(self.configs_path)
        self.configs_data.index = self.configs_data['Config Name']

        self.autofill_parameters = None
        self.window = None

        # list of signal parameters, sliders & constants
        self.param_names_list = None
        self.sliders_list = None
        self.constants_list = None
        self.values_to_set = None

        # Contructor procedure:
        self.config_name = None
        self.config_params = None


    @abstractmethod
    def ConnectCallBack(self, window):
        pass



    def init_autofill_parameters(self):
        self.autofill_parameters = [
        [self.values_to_set[i], self.constants_list[i], self.sliders_list[i]] for i in range(len(self.constants_list))
        ]

    @abstractmethod
    def get_config_name(self):
        pass

    def init_config_params(self):
        self.config_params = self.configs_data.loc[self.config_name]

    @abstractmethod
    def init_param_names_list(self):
        pass

    @abstractmethod
    def init_constants_list(self):
        pass

    @abstractmethod
    def init_sliders_list(self):
        pass

    def init_values_to_set(self):
        self.values_to_set = [self.config_params[param_name] for param_name in self.param_names_list]

    def AutoFill(self):
        try:
            self.config_name = self.get_config_name()
            self.init_config_params()
            self.init_param_names_list()
            self.init_constants_list()
            self.init_sliders_list()
            self.init_values_to_set()
            self.init_autofill_parameters()

            self.set_signal_parameters(
                self.autofill_parameters
            )
        except:
            loggers['Debug'].debug(f'AutoFillOperator: AutoFill: {sys.exc_info()}')

    def set_signal_parameters(self, value_widgets):
        for v in value_widgets:
            value_to_set = v[0]
            constant = v[1]
            slider = v[2]
            slider.setValue(value_to_set * constant)


