from unittest import TestCase
from unittest.mock import patch, Mock
from .route_transform import GoogleTransform
from model import TypeResult


class TestGoogleTransform(TestCase):
    __response = """
            {
               "destination_addresses" : [ "1" ],
               "origin_addresses" : [ "1" ],
               "rows" : [
                  {
                     "elements" : [
                        {
                           "distance" : {
                              "text" : "1 km",
                              "value" : 1
                           },
                           "duration" : {
                              "text" : "0 mins",
                              "value" : 0
                           },
                           "status" : "OK"
                        }
                     ]
                  }
               ],
               "status" : "OK"
            }
            """

    @patch('requests.get')
    def test_create_distance_matrix_distance(self, request_mock: Mock):
        request_mock.return_value.content = self.__response

        request_data = ['1']

        transform = GoogleTransform()
        matrix = transform.create_distance_matrix(data_raw=request_data, type_matrix=TypeResult.Distance)

        self.assertEqual(len(matrix), 1)
        self.assertEqual(matrix[0][0], 1)

    @patch('requests.get')
    def test_create_distance_matrix_duration(self, request_mock: Mock):
        request_mock.return_value.content = self.__response

        request_data = ['1']

        transform = GoogleTransform()
        matrix = transform.create_distance_matrix(data_raw=request_data, type_matrix=TypeResult.Time)

        self.assertEqual(len(matrix), 1)
        self.assertEqual(matrix[0][0], 0)
