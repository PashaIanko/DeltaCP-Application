import pandas as pd


class SendingLogger:
    def __init__(self):
        self.f_real = []
        self.f_expect = []
        self.t_real = []
        self.t_expect = []
        self.cycle_real_dts = []
        self.cycle_expect_dts = []

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
        self.cycle_real_dts.clear()
        self.cycle_expect_dts.clear()


    def save_database(self):
        # Перед сохранением нужна предобработка
        # Графу времени перевести в секунды и сдвинуть на константу (
        # Синхронизовать начало отсчёта реальных и ожидаемых данных)
        # Добавить в новую колонку и сохранить

        real_shifted_seconds = self.process_time_column()

        a = {
            'Expect Time': self.t_expect,
            'Expect Freq, Hz': self.f_expect,

            'Real Time (Synchronized), Sec': real_shifted_seconds,
            'Real Freq, Hz': self.f_real,

            'Real Time, Sec': self.t_real,

            'Cycle dt real, Sec': self.cycle_real_dts,
            'Cycle dt expect, Sec': self.cycle_expect_dts
        }
        df = pd.DataFrame.from_dict(a, orient='index')
        df = df.transpose()

        # df = pd.DataFrame({
        #     'Expect Time': self.t_expect,
        #     'Expect Freq, Hz': self.f_expect,
        #
        #     'Real Time (Synchronized), Sec': real_shifted_seconds,
        #     'Real Freq, Hz': self.f_real,
        #
        #     'Real Time, Sec': self.t_real,
        #
        #     'Cycle dt, Sec': self.cycle_dts
        # })
        df.to_excel(self.output_filename, index=False)


    def log(self, f_expect, f_real, t_expect, t_real):
        self.f_expect.append(f_expect)
        self.f_real.append(f_real)
        self.t_real.append(t_real)
        self.t_expect.append(t_expect)

    def log_cycle_time(self, dt_real, dt_expect):
        self.cycle_real_dts.append(dt_real)
        self.cycle_expect_dts.append(dt_expect)

    def process_time_column(self):

        # преобразуем в секунды и сдвинем
        t_start = self.t_real[0]
        t_start_sec = (t_start.hour * 60 + t_start.minute) * 60 + t_start.second + 0.000001 * t_start.microsecond
        dt_shift = t_start_sec - self.t_expect[0]

        res = []
        for t in self.t_real:
            val = ((t.hour * 60 + t.minute) * 60 + t.second + 0.000001 * t.microsecond) - dt_shift  #  Перевод в секунды и сдвиг
            res.append(val)
        return res
