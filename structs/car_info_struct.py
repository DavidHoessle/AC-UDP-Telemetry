from data_types import StringType, IntType, FloatType, BoolType, ArrayType


car_info_struct = {
        "identifier": StringType(0, 2),
        "size": IntType(2),

        "speed_Kmh": FloatType(6),
        "speed_Mph": FloatType(10),
        "speed_Ms": FloatType(14),

        "isAbsEnabled": BoolType(18),
        "isAbsInAction": BoolType(19),
        "isTcInAction": BoolType(20),
        "isTcEnabled": BoolType(21),
        "isInPit": BoolType(22),
        "isEngineLimiterOn": BoolType(23),

        "accG_vertical": FloatType(24),
        "accG_horizontal": FloatType(28),
        "accG_frontal": FloatType(32),

        "lapTime": IntType(36),
        "lastLap": IntType(40),
        "bestLap": IntType(44),
        "lapCount": IntType(48),

        "gas": FloatType(52),
        "brake": FloatType(56),
        "clutch": FloatType(60),
        "engineRPM": FloatType(64),
        "steer": FloatType(62),
        "gear": FloatType(66),
        "cgHeight": FloatType(70),

        "wheelAngularSpeed": ArrayType(74, 4, FloatType),
        "slipAngle": ArrayType(90, 4, FloatType),
        "slipAngle_ContactPatch": ArrayType(106, 4, FloatType),
        "slipRatio": ArrayType(132, 4, FloatType),
        "tyreSlip": ArrayType(148, 4, FloatType),
        "ndSlip": ArrayType(154, 4, FloatType),
        "load": ArrayType(170, 4,  FloatType),
        "Dy": ArrayType(186, 4, FloatType),
        "Mz": ArrayType(202, 4, FloatType),
        "tyreDirtyLevel": ArrayType(218, 4, FloatType),

        "camberRAD": ArrayType(234, 4, FloatType),
        "tyreRadius": ArrayType(250, 4, FloatType),
        "tyreLoadedRadius": ArrayType(266, 4, FloatType),

        "suspensionHeight": ArrayType(282, 4, FloatType),
        "carPositionNormalized": FloatType(298),
        "carSlope": FloatType(302),
        "carCoordinates": ArrayType(306, 4, FloatType),
    }