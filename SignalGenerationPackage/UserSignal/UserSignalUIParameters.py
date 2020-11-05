
class UserSignalUIParameters:

    # ACCELERATION
    AccelerationTimeMin = 0.1
    AccelerationTimeMax = 600.0
    AccelerationTimeLineEditAccuracy = 2

    AccelerationTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    AccelerationTimeSliderMin = AccelerationTimeMin * AccelerationTimeCalcConstant
    AccelerationTimeSliderMax = AccelerationTimeMax * AccelerationTimeCalcConstant


    # DECELERATION
    DecelerationTimeMin = 0.1
    DecelerationTimeMax = 600.0
    DecelerationTimeLineEditAccuracy = 2

    DecelerationTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    DecelerationTimeSliderMin = DecelerationTimeMin * DecelerationTimeCalcConstant
    DecelerationTimeSliderMax = DecelerationTimeMax * DecelerationTimeCalcConstant

    def __init__(self):
        pass