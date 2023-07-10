from enum import Enum
from typing import List
from .vehicle_path import VehiclePath


class ResultSolver:
    __num_vehicles: int
    __nodes: List[str]
    __type_result: str
    __result_path: List[VehiclePath]
    __total: int

    @property
    def num_vehicles(self) -> int:
        return self.__num_vehicles

    @num_vehicles.setter
    def num_vehicles(self, num: int):
        self.__num_vehicles = num

    @property
    def nodes(self) -> List[str]:
        return self.__nodes

    @nodes.setter
    def nodes(self, nodes: List[str]):
        self.__nodes = nodes

    @property
    def type_result(self) -> str:
        return self.__type_result

    @type_result.setter
    def type_result(self, type_res: str):
        self.__type_result = type_res

    @property
    def result_path(self) -> List[VehiclePath]:
        return self.__result_path

    @result_path.setter
    def result_path(self, result: List[VehiclePath]):
        self.__result_path = result

    @property
    def total(self) -> int:
        return self.__total

    @total.setter
    def total(self, total: int):
        self.__total = total

    def num_nodes(self):
        return len(self.__nodes) if self.__nodes else 0


class TypeResult(Enum):
    Distance = 'Distance'
    Time = 'Time'
