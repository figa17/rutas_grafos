import logging
from model import ResultSolver
import graphviz
from pandas import DataFrame


def draw_graph_distance(distance_matrix: DataFrame, data: DataFrame):
    graph = graphviz.Digraph('Distance Matrix', format='png')
    graph.attr('node', shape='doublecircle')

    # data['distance'] = distance_matrix.iloc[:, 0]
    len_data = len(distance_matrix)
    for index, row in distance_matrix.iterrows():
        first_node = int(index) + 1
        for i in range(first_node, len_data):
            # logging.info(f'node {index} -> node {i} ==> distance: {row[i]}')
            if row[i] < 4.2:
                logging.info(f'node {index} -> node {i} ==> distance: {row[i]}')
                graph.edge(f'node {index}', f'node {i}', label=str(row[i]))

    graph.render(filename='di_graph', directory='data', overwrite_source=True)
    return graph


def add_result(graph: graphviz.Graph, result: ResultSolver):
    v_path = result.result_path[0]
    route = v_path.path
    total_dest = len(route)
    for i in range(total_dest):
        if i + 1 < total_dest:
            graph.edge(f'node {route[i]}', f'node {route[i + 1]}', color="red")

    graph.render(filename='di_graph_result', directory='data', overwrite_source=True)
