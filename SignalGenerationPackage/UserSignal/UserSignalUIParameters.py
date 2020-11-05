
class UserSignalUIParameters:

    AccelerationTimeMin = 0.1
    AccelerationTimeMax = 600.0
    AccelerationTimeLineEditAccuracy = 2

    AccelerationTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    AccelerationTimeSliderMin = AccelerationTimeMin * AccelerationTimeCalcConstant
    AccelerationTimeSliderMax = AccelerationTimeMax * AccelerationTimeCalcConstant

    def __init__(self):
        pass