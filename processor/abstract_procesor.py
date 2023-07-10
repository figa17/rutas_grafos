from abc import ABC, abstractmethod
from model import RequestSolver, ResultSolver


class AbstractProcessor(ABC):

    @abstractmethod
    def process(self, request: RequestSolver) -> ResultSolver:
        pass
