from data_types.base_type import BaseType


class StringType(BaseType):
    def __init__(self, start: int, stop: int) -> None:
        super().__init__(start)
        self.size = stop - start

    @staticmethod
    def convert(x: bytearray) -> str:
        string = "".join(x.decode("utf-16"))
        end = string.find("%")
        if end >= 0:
            string = string[:end]
        return string
