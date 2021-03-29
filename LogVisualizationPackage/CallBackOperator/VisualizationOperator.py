from CallBackOperator import CallBackOperator
import pandas as pd
from PopUpNotifier.PopUpNotifier import PopUpNotifier

class VisualizationOperator(CallBackOperator):
    def __init__(self, DebugMode=False):
        self.DebugMode = DebugMode
        self.UserInterface = None
        self.NecessaryColumns = [
            'Expect Time',
            'Expect Freq, Hz',
            'Real Time (Synchronized), Sec',
            'Real Freq, Hz'
        ]  # Необходимые имена колонок



    def ConnectCallBack(self, UserInterface):
        UserInterface.VisualizeLogpushButton.clicked.connect(self.VisualizeLog)
        self.UserInterface = UserInterface

    def VisualizeLog(self):
        logfile_dir = self.UserInterface.LogFilenamelineEdit.text() + '.xlsx'

        log_plot = self.UserInterface.LogPlot
        log_plot.set_up_plot()
        real_t_label = self.UserInterface.RealTimelabel
        expect_t_label = self.UserInterface.ExpectTimelabel

        try:
            log_df = pd.read_excel(logfile_dir)
            cols_correct = self.check_columns_correctness(log_df)

            if cols_correct:
                t_expect = log_df['Expect Time'].values
                f_expect = log_df['Expect Freq, Hz'].values
                t_real = log_df['Real Time (Synchronized), Sec'].values

                if self.DebugMode:
                    f_real = f_expect
                else:
                    f_real = log_df['Real Freq, Hz'].values

                whole_t_real = self.calc_time_representation(t_real[-1])
                whole_t_expect = self.calc_time_representation(t_expect[-1])

                expect_t_label.setText(whole_t_expect)
                real_t_label.setText(whole_t_real)

                log_plot.plot(t_expect, f_expect, do_cla=False, label='Expect', marker='o', markersize=4)
                log_plot.plot(t_real, f_real, do_cla=False, label='Real', marker='o', markersize=4)

        except FileNotFoundError:
            PopUpNotifier.Error(f'Cannot find file {logfile_dir}')
        except:
            import sys
            print(sys.exc_info())

    @staticmethod
    def calc_time_representation(val_in_sec):
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

