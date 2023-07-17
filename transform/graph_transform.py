from pandas import DataFrame
import networkx as nx
import networkx.algorithms.approximation as nx_app
import logging
from .abstract_transform import AbstractGraphTransform
import matplotlib.pyplot as plt


class GraphTransform(AbstractGraphTransform):

    def create_graph(self, distance_matrix: DataFrame) -> nx.Graph:
        graph = nx.Graph()

        len_data = len(distance_matrix)
        for index, row in distance_matrix.iterrows():
            first_node = int(index) + 1
            for i in range(first_node, len_data):
                # logging.info(f'node {index} -> node {i} ==> distance: {row[i]}')
                # if row[i] < 4.2:
                logging.info(f'node {index} -> node {i} ==> distance: {row[i]}')
                graph.add_edge(index, i, weight=row[i])

        return graph