from SignalGenerationPackage.Point import Point
from SignalGenerationPackage.SignalTransformer import SignalTransformer

class EdgeSignalTransformer (SignalTransformer):
    # На этапе SignalGeneration мы создаём сигнал
    # Но перед отправкой, необходимо его преобразовать -
    # т.е. сдвинуть сигнал "влево" для отправки наперёд,
    # оптимизировать (удалить) повторяющиеся точки на плато
    # и на старте, чтоб не тратить лишнее время на их отправку.
    # Этим преобразованием и занимается Transformer

    def __init__(self, SignalData):
        super().__init__(SignalData)

    # overridden
    def TransformSignal(self):
        # Как должна выглядеть оптимизированная
        # Трапеция, если все времёна != 0

        y_optimized = [
            None,
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

        point_arr = self.SignalData.transformed_point_array
        if len(self.SignalData.point_array) >= len(y_optimized):
            for i in range (len(y_optimized)):
                if y_optimized[i] is None:
                    p = Point(x=self.SignalData.point_array[i].x, y=y_optimized[i], to_send=False)
                else:
                    p = Point(x=self.SignalData.point_array[i].x, y=y_optimized[i], to_send=True)
                point_arr.append(p)