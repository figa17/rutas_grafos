from ortools.constraint_solver.pywrapcp import Assignment
from model import ResultSolver, TypeResult, VehiclePath
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from pandas import DataFrame
from .abstract_solver import AbstractSolver
import logging


class RouteSolver(AbstractSolver):
    __solution: Assignment

    def __init__(self, distance_matrix: DataFrame, num_vehicles: int, index_depot: int,
                 result_type: TypeResult = None):
        self.__num_data = len(distance_matrix)
        self.__num_vehicles = num_vehicles
        self.__type_result = result_type if result_type else TypeResult.Distance
        self.__distance_matrix = distance_matrix.values.tolist()
        self.__manager = pywrapcp.RoutingIndexManager(self.__num_data, num_vehicles, index_depot)
        self.__index_depot = index_depot
        # Create Routing Model.
        self.__routing = pywrapcp.RoutingModel(self.__manager)
        logging.info(
            f'num_data: {self.__num_data}, num_vehicles: {self.__num_vehicles}, index_depot: {self.__index_depot}')

    def distance_callback(self, from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = self.__manager.IndexToNode(from_index)
        to_node = self.__manager.IndexToNode(to_index)
        return self.__distance_matrix[from_node][to_node]

    def solve(self):
        transit_callback_index = self.__routing.RegisterTransitCallback(self.distance_callback)

        # Define cost of each arc.
        self.__routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Add Distance constraint.
        dimension_name = self.__type_result.name
        # self.routing.AddDimension(
        #     transit_callback_index,
        #     0,  # no slack
        #     10000,  # vehicle maximum travel distance
        #     True,  # start cumul to zero
        #     self.dimension_name)
        #
        # distance_dimension = self.routing.GetDimensionOrDie(self.dimension_name)
        # distance_dimension.SetGlobalSpanCostCoefficient(100)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

        # Solve the problem.
        self.__solution = self.__routing.SolveWithParameters(search_parameters)

        # logging.info(solution   )
        # # Print solution on console.

    def get_best(self) -> ResultSolver:
        result_solver = ResultSolver(num_vehicles=self.__num_vehicles,
                                     nodes=self.__distance_matrix[0],
                                     type_result=self.__type_result)

        if self.__solution:
            max_route_distance = 0
            t_paths = []
            for vehicle_id in range(self.__num_vehicles):

                index = self.__routing.Start(vehicle_id)
                plan_output = []
                route_distance = 0
                while not self.__routing.IsEnd(index):
                    plan_output.append(self.__manager.IndexToNode(index))
                    previous_index = index
                    index = self.__solution.Value(self.__routing.NextVar(index))
                    route_distance += self.__routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
                plan_output.append(self.__index_depot)
                v_path = VehiclePath(index=vehicle_id, path=plan_output)
                logging.info(plan_output)
                max_route_distance = max(route_distance, max_route_distance)
                t_paths.append(v_path)

            result_solver.result_path = t_paths
            result_solver.total = max_route_distance

            return result_solver
        else:
            result_solver.result_path = []
            result_solver.total = 0
            return result_solver
