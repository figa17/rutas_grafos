from abc import ABC, abstractmethod
from typing import List
from model import TypeResult
from pandas import DataFrame


class AbstractTransform(ABC):

    @abstractmethod
    def create_distance_matrix(self, data_raw: DataFrame, type_matrix: TypeResult) -> List[List[int]]:
        pass
