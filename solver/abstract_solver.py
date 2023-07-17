from abc import ABC, abstractmethod
from typing import List
from model import ResultSolver


class AbstractSolver(ABC):

    @abstractmethod
    def solve(self) -> None:
        raise NotImplemented('Not implemented solver')

    @abstractmethod
    def get_best(self) -> ResultSolver:
        raise NotImplemented('Not implemented solver')
