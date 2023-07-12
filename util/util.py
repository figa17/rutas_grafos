import logging

import graphviz
from pandas import DataFrame


def draw_graph_distance(distance_matrix: DataFrame, data: DataFrame):
    graph = graphviz.Graph('Distance Matrix', format='png')
    graph.attr('node', shape='doublecircle')

    data['distance'] = distance_matrix.iloc[:, 0]
    len_data = len(distance_matrix)
    for index, row in distance_matrix.iterrows():
        first_node = int(index) + 1
        for i in range(first_node, len_data):
            logging.info(f'node {index} -> node {i} ==> distance: {row[i]}')
            if row[i] < 10000:
                graph.edge(f'node {index}', f'node {i}')

    graph.render(directory='data', overwrite_source=True)
