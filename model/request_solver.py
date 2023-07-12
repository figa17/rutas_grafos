from typing import List
from dataclasses import dataclass
from model import TypeResult


@dataclass
class RequestSolver:
    raw_data: List[str]
    num_vehicles: int
    index_depot: int
    type_result: TypeResult


