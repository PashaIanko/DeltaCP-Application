
class UserSignalUIParameters:

    # ACCELERATION TIME
    AccelerationTimeMin = 0.1
    AccelerationTimeMax = 600.0
    AccelerationTimeLineEditAccuracy = 2

    AccelerationTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    AccelerationTimeSliderMin = AccelerationTimeMin * AccelerationTimeCalcConstant
    AccelerationTimeSliderMax = AccelerationTimeMax * AccelerationTimeCalcConstant


    # PLATEAU TIME
    PlateauTimeMin = 0.0
    PlateauTimeMax = 600.0
    PlateauTimeLineEditAccuracy = 2

    PlateauTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    PlateauTimeSliderMin = PlateauTimeMin * PlateauTimeCalcConstant
    PlateauTimeSliderMax = PlateauTimeMax * PlateauTimeCalcConstant


    # DECELERATION TIME
    DecelerationTimeMin = 0.1
    DecelerationTimeMax = 600.0
    DecelerationTimeLineEditAccuracy = 2

    DecelerationTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    DecelerationTimeSliderMin = DecelerationTimeMin * DecelerationTimeCalcConstant
    DecelerationTimeSliderMax = DecelerationTimeMax * DecelerationTimeCalcConstant


    # END TIME
    EndTimeMin = 0.1
    EndTimeMax = 600.0
    EndTimeLineEditAccuracy = 2

    EndTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    EndTimeSliderMin = EndTimeMin * EndTimeCalcConstant
    EndTimeSliderMax = EndTimeMax * EndTimeCalcConstant

    # START TIME
    StartTimeMin = 0.1
    StartTimeMax = 600.0
    StartTimeLineEditAccuracy = 2

    StartTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    StartTimeSliderMin = StartTimeMin * StartTimeCalcConstant
    StartTimeSliderMax = StartTimeMax * StartTimeCalcConstant


    # LOW LEVEL
    LowLevelFrequencyMin = 0.1
    LowLevelFrequencyMax = 600.0
    LowLevelFrequencyLineEditAccuracy = 2

    LowLevelFrequencyCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    LowLevelFrequencySliderMin = LowLevelFrequencyMin * LowLevelFrequencyCalcConstant
    LowLevelFrequencySliderMax = LowLevelFrequencyMax * LowLevelFrequencyCalcConstant


    # HIGH LEVEL
    HighLevelFrequencyMin = 0.1
    HighLevelFrequencyMax = 600.0
    HighLevelFrequencyLineEditAccuracy = 2

    HighLevelFrequencyCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    HighLevelFrequencySliderMin = HighLevelFrequencyMin * HighLevelFrequencyCalcConstant
    HighLevelFrequencySliderMax = HighLevelFrequencyMax * HighLevelFrequencyCalcConstant


    # POINTS NUMBER
    PointsNumberMin = 5
    PointsNumberMax = 200
    PointsNumberLineEditAccuracy = 0

    PointsNumberCalcConstant = 1
    PointsNumberSliderMin = PointsNumberMin * PointsNumberCalcConstant
    PointsNumberSliderMax = PointsNumberMax * PointsNumberCalcConstant


    # VERTICAL OFFSET
    VerticalOffsetMin = 0
    VerticalOffsetMax = 20
    VerticalOffsetLineEditAccuracy = 1

    VerticalOffsetCalcConstant = 10
    VerticalOffsetSliderMin = VerticalOffsetMin * VerticalOffsetCalcConstant
    VerticalOffsetSliderMax = VerticalOffsetMax * VerticalOffsetCalcConstant
    

    def __init__(self):
        pass