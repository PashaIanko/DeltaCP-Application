import pandas as pd


class SendingLogger:
    def __init__(self):
        self.f_real = []
        self.f_expect = []
        self.t_real = []
        self.t_expect = []

        #self._dataframe = pd.DataFrame(
        #    {
        #        'Desired Freq, Hz': [],
        #        'Actual Freq, Hz': [],
        #        'Desired Time': [],
        #        'Actual Time': []
        #    }
        #)
        #self._output_filename = ''

    @property
    def output_filename(self):
        return self._output_filename

    @output_filename.setter
    def output_filename(self, val):
        self._output_filename = val

    def start_database(self):
        self.f_expect.clear()
        self.f_real.clear()
        self.t_expect.clear()
        self.t_real.clear()


    def save_database(self):
        df = pd.DataFrame({
            'Expect Freq, Hz': self.f_expect,
            'Actual Freq, Hz': self.f_real,
            'Desired Time': self.t_expect,
            'Actual Time': self.t_real
        })
        df.to_excel(self.output_filename, index=False)

    def log(self, f_expect, f_real, t_expect, t_real):
        self.f_expect.append(f_expect)
        self.f_real.append(f_real)
        self.t_real.append(t_real)
        self.t_expect.append(t_expect)

