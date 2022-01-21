from data_types import StringType, IntType


handshake_struct = {
    "carName": StringType(0, 100),
    "driverName": StringType(100, 200),
    "identifier": IntType(200, 204),
    "version": IntType(204, 208),
    "trackName": StringType(208, 308),
    "trackConfig": StringType(308, 408)
}