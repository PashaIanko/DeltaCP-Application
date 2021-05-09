from SignalGenerationPackage.SignalTransformer import SignalTransformer
from SignalGenerationPackage.Point import Point


class ExperimentScheduleTransformer(SignalTransformer):
    def __init__(self, SignalData):
        super().__init__(SignalData)

    # overridden
    def TransformSignal(self):
        point_arr = self.SignalData.point_array
        transformed_point_arr = self.SignalData.transformed_point_array

        points_len = len(point_arr)
        for i in range(points_len):
            if i == points_len - 1:
                p = Point(x=point_arr[i].x, y=point_arr[i].y, to_send=False)  # Последнюю точку отправлять не надо
            else:
                p = Point(x=point_arr[i].x, y=point_arr[i].y, to_send=True)
            transformed_point_arr.append(p)
