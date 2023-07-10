from abc import ABC, abstractmethod
from typing import List
from model import ResultSolver


class AbstractSolver(ABC):

    @abstractmethod
    def solve(self) -> List:
        pass

    @abstractmethod
    def get_best(self) -> ResultSolver:
        pass
