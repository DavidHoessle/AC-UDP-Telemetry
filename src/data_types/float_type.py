import struct
from data_types.base_type import BaseType


class FloatType(BaseType):
    size: int = 4

    def __init__(self, start: int) -> None:
        super().__init__(start)

    @staticmethod
    def convert(x: bytearray) -> float:
        return struct.unpack("f", x)[0]
