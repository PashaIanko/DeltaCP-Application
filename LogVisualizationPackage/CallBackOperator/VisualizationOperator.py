from CallBackOperator import CallBackOperator
import pandas as pd

class VisualizationOperator(CallBackOperator):
    def __init__(self):
        self.UserInterface = None



    def ConnectCallBack(self, UserInterface):
        UserInterface.VisualizeLogpushButton.clicked.connect(self.VisualizeLog)
        self.UserInterface = UserInterface

    def VisualizeLog(self):
        logfile_dir = self.UserInterface.LogFilenamelineEdit.text() + '.xlsx'
        log_plot = self.UserInterface.LogPlot
        try:


            log_df = pd.read_excel(logfile_dir)
            t_expect = log_df['Expect Time'].values
            f_expect = log_df['Expect Freq, Hz'].values
            t_real = log_df['Real Time (Synchronized), Sec'].values
            f_real = log_df['Real Freq, Hz'].values

            log_plot.plot(t_expect, f_expect)
            #log_plot.plot(t_real, f_real)

        except:
            import sys
            print(sys.exc_info())

