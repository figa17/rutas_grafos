from model import RequestSolver, ResultSolver
from transform import GoogleTransform
from solver import RouteSolver
from .abstract_procesor import AbstractProcessor


class RouteProcessor(AbstractProcessor):

    def process(self, request: RequestSolver) -> ResultSolver:
        data_raw = request.raw_data
        transform = GoogleTransform()
        distance = transform.create_distance_matrix(data_raw, request.type_result)
        solver = RouteSolver(distance_matrix=distance, num_vehicles=request.num_vehicles, index_depot=request.index_depot, result_type=request.type_result)
        solver.solve()

        return solver.get_best()
