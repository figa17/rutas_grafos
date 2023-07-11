import requests
import logging
import json
from config import CONFIG_GOOGLE
from typing import List
from model import TypeResult
from .abstract_transform import AbstractTransform
from pandas import DataFrame


class GoogleTransform(AbstractTransform):
    key_route = CONFIG_GOOGLE['route_key']

    def create_distance_matrix(self, data_raw: DataFrame, type_matrix: TypeResult) -> List[List[int]]:
        """

        :param type_matrix:
        :param data_raw:
        :return:
        """
        addresses = [item.lower().replace(' ', '+') for item in data_raw['Direccion']]
        # Distance Matrix API only accepts 100 elements per request, so get rows in multiple requests.
        max_elements = 100
        num_addresses = len(addresses)  # 16 in this example.
        # Maximum number of rows that can be computed per request (6 in this example).
        max_rows = max_elements // num_addresses
        # num_addresses = q * max_rows + r (q = 2 and r = 4 in this example).
        q, r = divmod(num_addresses, max_rows)
        dest_addresses = addresses
        distance_matrix = []
        # Send q requests, returning max_rows rows per request.
        for i in range(q):
            origin_addresses = addresses[i * max_rows: (i + 1) * max_rows]
            response = self.send_request(origin_addresses, dest_addresses)
            distance_matrix += self.build_distance_matrix(response, type_matrix)

        # Get the remaining remaining r rows, if necessary.
        if r > 0:
            origin_addresses = addresses[q * max_rows: q * max_rows + r]
            response = self.send_request(origin_addresses, dest_addresses)
            distance_matrix += self.build_distance_matrix(response, type_matrix)
        return distance_matrix

    def send_request(self, origin_addresses: List[str], dest_addresses: List[str]):
        """

        :param origin_addresses:
        :param dest_addresses:
        :return:
        """
        """ Build and send request for the given origin and destination addresses."""

        origin_address_str = self.build_address_str(origin_addresses)
        dest_address_str = self.build_address_str(dest_addresses)

        request = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin_address_str}&destinations={dest_address_str}&key={self.key_route}'
        json_result = requests.get(request).content
        response = json.loads(json_result)

        if response['status'] == 'OK':
            return response
        else:
            logging.error(response)
            raise Exception('Error al conectarse a la API de Google')

    def build_distance_matrix(self, response, type_matrix: TypeResult) -> List:
        distance_matrix = []
        for row in response['rows']:
            type_data = 'distance' if type_matrix == TypeResult.Distance else 'duration'
            row_list = [row['elements'][j][type_data]['value'] for j in range(len(row['elements']))]
            distance_matrix.append(row_list)
        return distance_matrix

    def build_address_str(self, addresses: List[str]) -> str:
        # Build a pipe-separated string of addresses
        address_str = ''
        for i in range(len(addresses) - 1):
            address_str += addresses[i] + '|'
        address_str += addresses[-1]
        return address_str
