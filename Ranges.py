class ValueRange:
    def __init__(self, min, max, decimals):
        self.min = min
        self.max = max
        self.decimals = decimals


class Ranges:
    frequency_range = ValueRange(min=0, max=50, decimals=2)