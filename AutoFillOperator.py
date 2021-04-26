from abc import ABC, abstractmethod
import pandas as pd
from LoggersConfig import loggers
from PopUpNotifier.PopUpNotifier import PopUpNotifier


class AutoFillOperator(ABC):
    def __init__(self, window, param_names, slider_text_pairs, model, configs_path):
        super().__init__()
        self.window = window
        self.model = model
        self.configs_path = configs_path
        self.configs_data = pd.read_excel(self.configs_path)
        self.configs_data.index = self.configs_data['Config Name']

        self.autofill_parameters = None
        self.config_line_edit = None  # текстовое поле с именем конфига

        # list of signal parameters, sliders
        self.param_names = param_names
        self.slider_text_pairs = slider_text_pairs
        self.sliders = [pair.slider for pair in self.slider_text_pairs]
        self.line_edits = [pair.line_edit for pair in self.slider_text_pairs]
        self.values_to_set = None

        # Contructor procedure:
        self.config_name = None
        self.config_params = None
        self.init_config_line_edit()

    @abstractmethod
    def init_config_line_edit(self):
        pass

    @abstractmethod
    def ConnectCallBack(self):
        pass

    def init_autofill_parameters(self):
        self.autofill_parameters = [
            [self.values_to_set[i] * self.slider_text_pairs[i].calc_constant, self.slider_text_pairs[i].slider] for i in
            range(len(self.slider_text_pairs))
        ]

    def get_config_name(self):
        return self.config_line_edit.text()

    def set_config_name(self, config_name):
        return self.config_line_edit.setText(config_name)

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
            PopUpNotifier.Warning(f'Preset "{self.config_name}" was not found in preset base!')
            loggers['Debug'].debug(f'AutoFillOperator: AutoFill: Preset {self.config_name} not found')

    def SavePreset(self):
        current_config_name = self.get_config_name()
        if current_config_name in self.configs_data['Config Name'].values:
            user_decision = PopUpNotifier.PresetSavingQUestion()
            if user_decision == True:
                self.RemovePreset(current_config_name)
                self.WriteNewPreset(current_config_name)
            else:
                return
        else:
            self.WriteNewPreset(current_config_name)

    def RemovePreset(self, config_name):  # Если config name не задан, то узнаем, что введено в текстовое поле --> удалим
        if config_name in self.configs_data['Config Name'].values:
            self.configs_data.drop([config_name], axis='index', inplace=True)
            self.configs_data.to_excel(self.configs_path, index=False)

    def DeletePreset(self):
        current_config_name = self.get_config_name()
        if current_config_name in self.configs_data['Config Name'].values:
            user_decision = PopUpNotifier.PresetDeleteQuestion(current_config_name)
            if user_decision == True:
                self.RemovePreset(current_config_name)
                self.ResetSliders(1)  # Чтобы после удаления пресета "обнулить" график, оставшийся от удалённого пресета
                self.set_config_name("")  # Обнулить имя конфига
        else:
            PopUpNotifier.Warning(f'Preset {current_config_name} was not found in preset base!')

    def ResetSliders(self, default_val):
        [slider.setValue(default_val) for slider in self.sliders]

    def WriteNewPreset(self, preset_name):
        values_to_add = self.read_values_from_gui()
        df_to_add = pd.DataFrame([[preset_name] + values_to_add],
                                 columns=['Config Name'] + self.param_names)
        df_to_add.index = df_to_add['Config Name']
        self.configs_data = self.configs_data.append(df_to_add)
        self.configs_data.to_excel(self.configs_path, index=False)

    def read_values_from_gui(self):
        values = []
        for line_edit in self.line_edits:
            text = line_edit.text()
            if text == '':
                val = 0
            else:
                val = float(text.replace(',', '.'))
            values.append(val)
        return values


    def set_signal_parameters(self, value_widgets):
        for v in value_widgets:
            value_to_set = v[0]
            slider = v[1]
            slider.setValue(value_to_set)

