

class DeltaCPRegisters:
    # Entity, contains registers of DeltaCP
    FrequencyCommandRegister = 0x2001  # To set frequency

    CurrentFrequencyRegister = 0x2103  # Истинная частота в данный момент времени
    SetFrequencyRegister = 0x2102  # То, что Delta CP 2000 считает заданной величиной (т.е.
                                    # Ты можешь задать невалидное значение, он его отфильтрует (F_max, F_min)
                                    # и выставит в 0x2103 то, что считает нужным)
    StartStopRegister = 0x2000  # Выставляем два последних (младших) бита, чтобы отправить RUN, STOP (Page 514/868 Manual)

    def __init__(self):
        pass