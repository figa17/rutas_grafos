from abc import ABC, abstractmethod
from typing import List
from model import TypeResult
from pandas import DataFrame
import networkx as nx


class AbstractTransform(ABC):

    @abstractmethod
    def create_distance_matrix(self, data_raw: DataFrame, type_matrix: TypeResult) -> List[List[int]]:
        raise NotImplemented('Not implemented transform')


class AbstractGraphTransform(ABC):

    @abstractmethod
    def create_graph(self, distance_matrix: DataFrame) -> nx.Graph():
        raise NotImplemented('Not implemented transform')
