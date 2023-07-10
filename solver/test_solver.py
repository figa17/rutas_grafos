from unittest import TestCase

from model import TypeResult
from solver import RouteSolver


class TestRouteSolver(TestCase):

    def test_get_best(self):
        test_distance = [
            [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
            [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
            [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
            [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
            [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
            [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
            [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
            [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
            [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
            [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
            [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
            [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
            [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
        ]

        solver = RouteSolver(test_distance, num_vehicles=1, index_depot=0, result_type=TypeResult.Distance)
        solver.solve()
        best_solution = solver.get_best()

        self.assertIsNotNone(best_solution)
        self.assertEqual(best_solution.total, 7293)
        self.assertEqual(best_solution.type_result, TypeResult.Distance)
        self.assertEqual(best_solution.nodes, 13)
        self.assertEqual(best_solution.num_vehicles, 1)

        best_path = best_solution.result_path
        # 0 -> 7 -> 2 -> 3 -> 4 -> 12 -> 6 -> 8 -> 1 -> 11 -> 10 -> 5 -> 9 -> 0
        self.assertEqual(len(best_path), 1)
        path = best_path[0]
        self.assertEqual(path.index, 0)
        self.assertEqual(len(path.path), 14)
        self.assertTrue(path.path == [0, 7, 2, 3, 4, 12, 6, 8, 1, 11, 10, 5, 9, 0])
