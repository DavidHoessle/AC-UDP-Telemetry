import struct
from data_types.base_type import BaseType


class BoolType(BaseType):
    size: int = 1

    def __init__(self, start: int) -> None:
        super().__init__(start)

    @staticmethod
    def convert(x: bytearray) -> bool:
        return struct.unpack("?", x)[0]
