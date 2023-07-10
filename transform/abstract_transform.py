from abc import ABC, abstractmethod
from typing import List

from model import TypeResult


class AbstractTransform(ABC):

    @abstractmethod
    def create_distance_matrix(self, data_raw: List[str], type_matrix: TypeResult) -> List[int]:
        pass
