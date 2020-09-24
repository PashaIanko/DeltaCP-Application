

class DeltaCPRegisters:
    # Entity, contains registers of DeltaCP
    FrequencyCommandRegister = 0x2001  # To set frequency
    CurrentFrequencyRegister = 0x2103
    SetFrequencyRegister = 0x2102  # Frequency Command, page 515/868 manual Delta CP 2000

    def __init__(self):
        pass