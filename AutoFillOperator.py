from abc import ABC, abstractmethod
import pandas as pd
from LoggersConfig import loggers
from PopUpNotifier.PopUpNotifier import PopUpNotifier

class AutoFillOperator(ABC):
    def __init__(self, slider_constants, param_names, sliders, model, configs_path):
        super().__init__()
        self.model = model
        self.configs_path = configs_path
        self.configs_data = pd.read_excel(self.configs_path)
        self.configs_data.index = self.configs_data['Config Name']

        self.autofill_parameters = None
        self.window = None

        # list of signal parameters, sliders & constants
        self.param_names = param_names
        self.sliders = sliders
        self.constants = slider_constants
        self.values_to_set = None

        # Contructor procedure:
        self.config_name = None
        self.config_params = None


    @abstractmethod
    def ConnectCallBack(self, window):  # TODO: Для autoFill кнопочку delete preset
        pass

    def init_autofill_parameters(self):
        self.autofill_parameters = [
            [self.values_to_set[i], self.constants[i], self.sliders[i]] for i in range(len(self.constants))
        ]

    @abstractmethod
    def get_config_name(self):
        pass

    def init_config_params(self):
        self.config_params = self.configs_data.loc[self.config_name]

    def init_values_to_set(self):
        self.values_to_set = [self.config_params[param_name] for param_name in self.param_names]

    def AutoFill(self):
        try:
            self.config_name = self.get_config_name()
            self.init_config_params()
            self.init_values_to_set()
            self.init_autofill_parameters()

            self.set_signal_parameters(
                self.autofill_parameters
            )
        except KeyError:
            loggers['Debug'].debug(f'AutoFillOperator: AutoFill: Preset {self.config_name} not found')

    def SavePreset(self):
        current_config_name = self.get_config_name()
        if current_config_name in self.configs_data['Config Name'].values:
            user_decision = PopUpNotifier.PresetSavingQUestion()
            if user_decision == True:
                self.DeletePreset(current_config_name)
                self.WriteNewPreset(current_config_name)
            else:
                return
        else:
            self.WriteNewPreset(current_config_name)

    def DeletePreset(self, config_name):
        self.configs_data.drop([config_name], axis='index', inplace=True)
        self.configs_data.to_excel(self.configs_path, index=False)

    def WriteNewPreset(self, preset_name):
        values_to_add = self.read_values_from_gui()
        df_to_add = pd.DataFrame([[preset_name] + values_to_add],
                                 columns=['Config Name'] + self.param_names)
        df_to_add.index = df_to_add['Config Name']
        self.configs_data = self.configs_data.append(df_to_add)
        self.configs_data.to_excel(self.configs_path, index=False)

    def read_values_from_gui(self):
        return [slider.value() / normalize_const for slider, normalize_const in zip(self.sliders, self.constants)]

    def set_signal_parameters(self, value_widgets):
        for v in value_widgets:
            value_to_set = v[0]
            constant = v[1]
            slider = v[2]
            slider.setValue(value_to_set * constant)


