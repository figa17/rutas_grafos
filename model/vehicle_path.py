from typing import List


class VehiclePath:
    __index: int
    __path: List[int]

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def path(self) -> List[int]:
        return self.__path

    @path.setter
    def path(self, path: List[int]):
        self.__path = path
