import unittest
from unittest.mock import MagicMock, patch
from geoserver.geomesh import Geomesh

class TestGeomesh(unittest.TestCase):
    def setUp(self):
        self.geomesh = Geomesh(geo_out_db_dir='test_db')

    @patch('geoserver.geomesh.shape.Shape')
    def test_filter(self, mock_shape):
        mock_shape_instance = mock_shape.return_value
        mock_shape_instance.get_h3_in_shape.return_value = ['test_cell']
        result = self.geomesh.filter('test_shapefile', resolution=8)
        self.assertEqual(result, ['test_cell']) 