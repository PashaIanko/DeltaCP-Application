class ValueRange:
    def __init__(self, min, max, decimals, calc_constant=100):

        # Если decimals == 2, то calc_constant должна быть 100
        # (Пределы слайдера умножаются на 10^(decimals))
        self.min = min
        self.max = max
        self.decimals = decimals
        self.calc_constant = calc_constant
        self.slider_min = min * calc_constant
        self.slider_max = max * calc_constant


class Ranges:
    frequency_range = ValueRange(min=0, max=50, decimals=2)

class EdgeSignalRanges:
    t_start_range = ValueRange(min=0, max=50, decimals=2)
    t_acceleration_range = ValueRange(min=0, max=80, decimals=2)
    t_plateau_range = ValueRange(min=0, max=80, decimals=2)
    t_deceleration_range = ValueRange(min=0, max=80, decimals=2)
    t_end_range = ValueRange(min=0, max=50, decimals=2)
    high_freq_range = ValueRange(min=0, max=50, decimals=2)
    low_freq_range = ValueRange(min=0, max=49, decimals=2)
    request_freq_range = ValueRange(min=0.3, max=1.0, decimals=2)
    flowrate_recalc_range = ValueRange(min=0.001, max=1000.0, decimals=3)