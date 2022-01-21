from typing import List, Union
from data_types.base_type import BaseType


class ArrayType(BaseType):
    def __init__(self, start: int, elems: int, obj_type: BaseType) -> None:
        super().__init__(start)
        self.obj_type = obj_type
        self.size = elems * obj_type.size

    @staticmethod
    def chunk(barray: bytearray, chunk_size: int) -> List[bytearray]:
        return [barray[i:i+chunk_size] for i in range(0, len(barray), chunk_size)]

    def convert(self, x: bytearray) -> List[Union[int, bool, float]]:
        return list(map(self.obj_type.convert, self.chunk(x, self.obj_type.size)))
