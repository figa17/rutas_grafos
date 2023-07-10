from typing import List

from model import TypeResult


class RequestSolver:
    __raw_data: List[str]
    __num_vehicles: int
    __index_depot: int
    __type_result: TypeResult

    @property
    def raw_data(self) -> List[str]:
        return self.__raw_data

    @raw_data.setter
    def raw_data(self, data: List[str]):
        self.__raw_data = data

    @property
    def num_vehicles(self) -> int:
        return self.__num_vehicles

    @num_vehicles.setter
    def num_vehicles(self, num: int):
        self.__num_vehicles = num

    @property
    def index_depot(self) -> int:
        return self.__index_depot

    @index_depot.setter
    def index_depot(self, index: int):
        self.__index_depot = index

    @property
    def type_result(self) -> TypeResult:
        return self.__type_result

    @type_result.setter
    def type_result(self, type_result: TypeResult):
        self.__type_result = type_result
