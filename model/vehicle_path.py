from typing import List
from dataclasses import dataclass


@dataclass
class VehiclePath:
    index: int
    path: List[int]
