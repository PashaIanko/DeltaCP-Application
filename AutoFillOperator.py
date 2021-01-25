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

        # Contructor procedure:
        self.config_name = None
        self.config_params = None


    @abstractmethod
    def ConnectCallBack(self, window):
        pass

    @abstractmethod
    def init_autofill_parameters(self):
        pass

    @abstractmethod
    def get_config_name(self):
        pass

    def get_config_params(self):
        return self.configs_data.loc[self.config_name]

    def AutoFill(self):
        try:
            self.config_name = self.get_config_name()
            self.config_params = self.get_config_params()
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


