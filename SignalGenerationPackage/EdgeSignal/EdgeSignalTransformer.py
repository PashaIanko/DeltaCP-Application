class EdgeSignalTransformer:
    # На этапе SignalGeneration мы создаём сигнал
    # Но перед отправкой, необходимо его преобразовать -
    # т.е. сдвинуть сигнал "влево" для отправки наперёд,
    # оптимизировать (удалить) повторяющиеся точки на плато
    # и на старте, чтоб не тратить лишнее время на их отправку.
    # Этим преобразованием и занимается Transformer

    def __init__(self, SignalData):
        self.SignalData = SignalData

    def TransformSignal(self):
        # Как должна выглядеть оптимизированная
        # Трапеция, если все времёна != 0

        y_optimized = [
            self.SignalData.LowLevelFrequency,
            self.SignalData.HighLevelFrequency,
            None,  # Повторяющаяся точка на плато
            self.SignalData.LowLevelFrequency,
            None,
            None
        ]

        if self.SignalData.PlateauTime == 0:
            del y_optimized[2]
        if self.SignalData.StartTime == 0:
            del y_optimized[0]
        if self.SignalData.EndTime == 0:
            del y_optimized[-1]

        self.SignalData.x_to_send = self.SignalData.x
        self.SignalData.y_to_send = y_optimized