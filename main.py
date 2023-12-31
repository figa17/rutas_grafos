import logging
from transform import GoogleTransform, GeoTransform, GraphTransform
from solver import RouteSolver, GraphSolver
from model import TypeResult
from util import draw_graph_distance, add_result
import pandas as pd
from os import path

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(name)s %(funcName)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

MATRIX_NAME_FILE_PATH = 'data/matrix.csv'


def main():
    data_raw = pd.read_csv('data/data.csv', sep=';')

    logging.info('main')

    if not path.isfile(MATRIX_NAME_FILE_PATH):
        logging.info('No existe archivo con datos')
        gTransform = GeoTransform()
        distance_matrix = gTransform.create_distance_matrix(data_raw, type_matrix=TypeResult.Distance)
        data = pd.DataFrame(distance_matrix)
        data.to_csv(MATRIX_NAME_FILE_PATH, sep=';', float_format='%.4f')
        logging.info('Escribiendo datas en archivo csv.')
    else:
        distance_matrix = pd.read_csv(MATRIX_NAME_FILE_PATH, sep=';', index_col=0)

    # draw = draw_graph_distance(distance_matrix, data_raw)

    """
    Example distance matrix 
    
    distance = [
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
    """
    # solver = RouteSolver(distance_matrix=distance_matrix, num_vehicles=1, index_depot=0)
    # solver.solve()
    #  GoogleTransform get_best- [0, 5, 3, 1, 10, 6, 15, 11, 4, 9, 7, 13, 8, 2, 14, 12, 0]
    #  GeoTransform    get_best- [0, 12, 14, 8, 2, 11, 9, 15, 1, 4, 5, 6, 7, 3, 13, 10, 0]
    #  nx                        [0, 10, 13, 9, 4, 15, 1, 5, 11, 6, 7, 3, 2, 14, 8, 12, 0]
    # result = solver.get_best()

    # add_result(draw, result)

    graph_transform = GraphTransform()
    graph = graph_transform.create_graph(distance_matrix)
    solver = GraphSolver(graph)
    solver.solve()
    result = solver.get_best()
    print(result.result_path)


if __name__ == '__main__':
    main()
