from CallBackOperator import CallBackOperator
import pandas as pd
from PopUpNotifier.PopUpNotifier import PopUpNotifier

class VisualizationOperator(CallBackOperator):
    def __init__(self):
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

        try:
            log_df = pd.read_excel(logfile_dir)
            cols_correct = self.check_columns_correctness(log_df)

            if cols_correct:
                t_expect = log_df['Expect Time'].values
                f_expect = log_df['Expect Freq, Hz'].values
                t_real = log_df['Real Time (Synchronized), Sec'].values
                f_real = log_df['Real Freq, Hz'].values

                log_plot.plot(t_expect, f_expect)
                #log_plot.plot(t_real, f_real)

        except FileNotFoundError:
            PopUpNotifier.Error(f'Cannot find file {logfile_dir}')
        except:
            import sys
            print(sys.exc_info())  # TODO: wrong filename PopUpNotifier сделать

    def check_columns_correctness(self, df):
        cols = df.columns
        for c in self.NecessaryColumns:
            if not c in cols:
                PopUpNotifier.Error(f'The .xlsx file does not have column "{c}".\nIncorrect source data!')
                return False
        return True

