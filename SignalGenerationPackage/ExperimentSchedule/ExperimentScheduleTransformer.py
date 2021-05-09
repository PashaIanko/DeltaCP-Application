from SignalGenerationPackage.SignalTransformer import SignalTransformer
from SignalGenerationPackage.Point import Point


class ExperimentScheduleTransformer(SignalTransformer):
    def __init__(self, SignalData):
        super().__init__(SignalData)

    # overridden
    def TransformSignal(self):
        # В функции UpdateSignalData мы создали
        # начальный сигнал, который записан в SignalData.point_array
        # надо его оптимизировать - какие точки отправлять, а какие нет
        point_arr = self.SignalData.point_array
        transformed_point_arr = self.SignalData.transformed_point_array

        points_len = len(point_arr)
        for i in range(points_len):
            if i == 0 or i == points_len - 1:  # Первую и последнюю точки отправлять не надо
                p = Point(x=point_arr[i].x, y=point_arr[i].y, to_send=False)
            else:
                # Структура сигнала - набор "полочек", плато
                # В начале каждой полочки (чётный i-индекс) надо задавать частоту
                if i % 2 == 0:
                    # Чётный индекс, по нему отправка значения
                    p = Point(x=point_arr[i].x, y=point_arr[i].y, to_send=True)
                else:
                    p = Point(x=point_arr[i].x, y=point_arr[i].y, to_send=False)
            transformed_point_arr.append(p)