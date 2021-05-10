from CallBackOperator import CallBackOperator
import pandas as pd
from PopUpNotifier.PopUpNotifier import PopUpNotifier
import numpy as np

class VisualizationOperator(CallBackOperator):
    def __init__(self, user_interface, DebugMode=False):
        super().__init__(user_interface, model=None, value_range=None)
        self.DebugMode = DebugMode


        self.NecessaryColumns = [
            'Expect Time',
            'Expect Freq, Hz',
            'Real Time (Synchronized), Sec',
            'Real Freq, Hz',
            'Cycle dt delay, Sec'
        ]  # Необходимые имена колонок

    def ConnectCallBack(self):
        self.window.VisualizeLogpushButton.clicked.connect(self.VisualizeLog)

    def VisualizeLog(self):
        logfile_dir = self.window.LogFilenamelineEdit.text() + '.xlsx'

        log_plot = self.window.LogPlot
        log_plot.set_up_plot()
        real_t_label = self.window.RealTimelabel
        expect_t_label = self.window.ExpectTimelabel
        sigma_label = self.window.StandardDeviationlabel
        avg_command_delay_label = self.window.AverageCommandDelaylabel
        cycle_delay_label = self.window.CycleDelaylabel

        try:
            log_df = pd.read_excel(logfile_dir)
            cols_correct = self.check_columns_correctness(log_df)

            if cols_correct:
                t_expect = log_df['Expect Time'].values
                f_expect = log_df['Expect Freq, Hz'].values
                t_real = log_df['Real Time (Synchronized), Sec'].values
                cycle_delays = log_df['Cycle dt delay, Sec'].values

                if self.DebugMode:
                    f_real = f_expect
                else:
                    f_real = log_df['Real Freq, Hz'].values

                standard_deviation = self.calc_standard_deviation(f_real, f_expect)
                sigma_label.setText(self.value_to_text(standard_deviation))

                average_cycle_dt_delay = self.calc_average_cycle_dt_delay(cycle_delays)
                cycle_delay_label.setText(self.calc_time_representation(average_cycle_dt_delay))

                average_command_delay = self.calc_average_command_delay(t_expect, t_real)
                avg_command_delay_label.setText(self.calc_time_representation(average_command_delay))

                whole_t_real = self.calc_time_representation(t_real[-1])
                real_t_label.setText(whole_t_real)

                whole_t_expect = self.calc_time_representation(t_expect[-1])
                expect_t_label.setText(whole_t_expect)


                log_plot.plot(t_expect, f_expect, do_cla=False, label='Expect', marker='o', markersize=4)
                log_plot.plot(t_real, f_real, do_cla=False, label='Real', marker='o', markersize=4)

        except FileNotFoundError:
            PopUpNotifier.Error(f'Cannot find file {logfile_dir}')
        except:
            import sys
            print(sys.exc_info())

    @staticmethod
    def calc_average_cycle_dt_delay(cycle_delays):
        valid_delays = [i for i in cycle_delays if not (np.isnan(i))]
        if len(valid_delays) > 0:
            return sum(valid_delays) / len(valid_delays)
        return None

    @staticmethod
    def calc_average_command_delay(arr1, arr2):
        if len(arr1) == len(arr2) and len(arr1) > 0:
            delays = [abs(i - j) for i, j in zip(arr1, arr2) if (not np.isnan(i) and not np.isnan(j))]
            return (sum(delays)) / (len(arr1))
        return None

    @staticmethod
    def value_to_text(value):
        if value is None:
            return ' '
        else:
            return f'{round(value, 2)}'

    @staticmethod
    def calc_standard_deviation(arr1, arr2):
        if len(arr1) == len(arr2) and len(arr1) > 0:
            diffs_squared = [(i - j)**2 for i, j in zip(arr1, arr2) if (not np.isnan(i) and not np.isnan(j))]
            return ((sum(diffs_squared)) / len(arr1)) ** (1/2)
        return None

    @staticmethod
    def calc_time_representation(val_in_sec):
        if val_in_sec is None or np.isnan(val_in_sec):
            return ' '
        hrs = int(val_in_sec / 3600)
        mins = int((val_in_sec - 3600 * hrs) / 60)
        secs = round(val_in_sec - 3600 * hrs - 60 * mins, 2)
        return f'{hrs} hr, {mins} min, {secs} sec'

    def check_columns_correctness(self, df):
        cols = df.columns
        for c in self.NecessaryColumns:
            if not c in cols:
                PopUpNotifier.Error(f'The .xlsx file does not have column "{c}".\nIncorrect source data!')
                return False
        return True


    # overridden
    def value_changed(self, val):
        pass

    # overridden
    def init_slider(self):
        pass

    # overridden
    def init_line_edit(self):
        pass