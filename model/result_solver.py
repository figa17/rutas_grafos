from enum import Enum
from typing import List
from .vehicle_path import VehiclePath
from dataclasses import dataclass, field


class TypeResult(Enum):
    Distance = 'Distance'
    Time = 'Time'


@dataclass
class ResultSolver:
    num_vehicles: int
    nodes: List[int]
    type_result: TypeResult
    result_path: List[VehiclePath] = field(init=False)
    total: int = field(init=False)

    def num_nodes(self):
        return len(self.nodes) if self.nodes else 0
