class DynamicPointsDensityUIParameters:
    # ACCELERATION TIME
    AccelerationTimeMin = 0.01
    AccelerationTimeMax = 300.0
    AccelerationTimeLineEditAccuracy = 2

    AccelerationTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    AccelerationTimeSliderMin = AccelerationTimeMin * AccelerationTimeCalcConstant
    AccelerationTimeSliderMax = AccelerationTimeMax * AccelerationTimeCalcConstant

    # PLATEAU TIME
    PlateauTimeMin = 0.0
    PlateauTimeMax = 300.0
    PlateauTimeLineEditAccuracy = 2

    PlateauTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    PlateauTimeSliderMin = PlateauTimeMin * PlateauTimeCalcConstant
    PlateauTimeSliderMax = PlateauTimeMax * PlateauTimeCalcConstant

    # DECELERATION TIME
    DecelerationTimeMin = 0.01
    DecelerationTimeMax = 300.0
    DecelerationTimeLineEditAccuracy = 2

    DecelerationTimeCalcConstant = 300  # Раз 100, значит цифры с точностью до 10**2
    DecelerationTimeSliderMin = DecelerationTimeMin * DecelerationTimeCalcConstant
    DecelerationTimeSliderMax = DecelerationTimeMax * DecelerationTimeCalcConstant

    # END TIME
    EndTimeMin = 0.0
    EndTimeMax = 300.0
    EndTimeLineEditAccuracy = 2

    EndTimeCalcConstant = 300  # Раз 100, значит цифры с точностью до 10**2
    EndTimeSliderMin = EndTimeMin * EndTimeCalcConstant
    EndTimeSliderMax = EndTimeMax * EndTimeCalcConstant

    # START TIME
    StartTimeMin = 0.0
    StartTimeMax = 300.0
    StartTimeLineEditAccuracy = 2

    StartTimeCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    StartTimeSliderMin = StartTimeMin * StartTimeCalcConstant
    StartTimeSliderMax = StartTimeMax * StartTimeCalcConstant

    # LOW LEVEL
    LowLevelFrequencyMin = 0.0
    LowLevelFrequencyMax = 20.0
    LowLevelFrequencyLineEditAccuracy = 2

    LowLevelFrequencyCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    LowLevelFrequencySliderMin = LowLevelFrequencyMin * LowLevelFrequencyCalcConstant
    LowLevelFrequencySliderMax = LowLevelFrequencyMax * LowLevelFrequencyCalcConstant

    # HIGH LEVEL
    HighLevelFrequencyMin = 0.0
    HighLevelFrequencyMax = 80.0
    HighLevelFrequencyLineEditAccuracy = 2

    HighLevelFrequencyCalcConstant = 100  # Раз 100, значит цифры с точностью до 10**2
    HighLevelFrequencySliderMin = HighLevelFrequencyMin * HighLevelFrequencyCalcConstant
    HighLevelFrequencySliderMax = HighLevelFrequencyMax * HighLevelFrequencyCalcConstant

    # POINTS DENSITY
    PointsDensityMin = 0
    PointsDensityMax = 3
    PointsDensityLineEditAccuracy = 2

    PointsDensityCalcConstant = 100
    PointsDensitySliderMin = PointsDensityMin * PointsDensityCalcConstant
    PointsDensitySliderMax = PointsDensityMax * PointsDensityCalcConstant

    # VERTICAL OFFSET
    VerticalOffsetMin = 0
    VerticalOffsetMax = 20
    VerticalOffsetLineEditAccuracy = 1

    VerticalOffsetCalcConstant = 10
    VerticalOffsetSliderMin = VerticalOffsetMin * VerticalOffsetCalcConstant
    VerticalOffsetSliderMax = VerticalOffsetMax * VerticalOffsetCalcConstant

    # PLOT PROPERTIES
    PlotHeight = 5
    PlotWidth = 5
    PlotXPosition = 0
    PlotYPosition = 320

    # REQUEST FREQUENCY
    RequestFreqLineEditAccuracy = 100
    RequestFreqCalcConstant = 10
    RequestFreqSliderMin = 0.1 * RequestFreqCalcConstant
    RequestFreqSliderMax = 1.1 * RequestFreqCalcConstant

    def __init__(self):
        pass
