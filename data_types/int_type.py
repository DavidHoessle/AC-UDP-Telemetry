from data_types.base_type import BaseType


class IntType(BaseType):
    size: int = 4

    def __init__(self, start: int) -> None:
        super().__init__(start)

    @staticmethod
    def convert(x: bytearray) -> int:
        return int.from_bytes(x, byteorder="little")
