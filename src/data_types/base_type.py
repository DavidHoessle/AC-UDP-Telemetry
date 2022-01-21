from typing import Slice, Union


class BaseType:
    range: Slice = None
    size: int = None

    def __init__(self, start: int) -> None:
        self.range = slice(start, start + self.size)

    @staticmethod
    def convert(x: bytearray) -> Union[int, bool, str, float]:
        raise NotImplementedError()

    def decode(self, data: bytearray) -> Union[int, bool, str, float]:
        return self.convert(data[self.range])
