import networkx.algorithms.approximation as nx_app
from model import ResultSolver, TypeResult
import networkx as nx
from .abstract_solver import AbstractSolver


class GraphSolver(AbstractSolver):

    def __init__(self, graph: nx.Graph, num_vehicles=1, type_result=TypeResult.Distance):
        self.__graph = graph
        self.__num_vehicles = num_vehicles
        self.__type_result = type_result
        self.__best = None

    def solve(self):
        """

        :return:

        References
        ----------
        .. [1] Christofides, Nicos. "Worst-case analysis of a new heuristic for
        the travelling salesman problem." No. RR-388. Carnegie-Mellon Univ
        Pittsburgh Pa Management Sciences Research Group, 1976.
        """
        self.__best = nx_app.christofides(self.__graph, weight="weight")

    def get_best(self) -> ResultSolver:
        max_route_distance = 0
        result_solver = ResultSolver(num_vehicles=self.__num_vehicles,
                                     nodes=self.__graph.nodes(),
                                     type_result=self.__type_result)

        if not self.__best:
            result_solver.result_path = []
            result_solver.total = 0
            return result_solver

        edge_list = list(nx.utils.pairwise(self.__best))
        result_solver.result_path = self.__best
        result_solver.total = max_route_distance

        return result_solver
