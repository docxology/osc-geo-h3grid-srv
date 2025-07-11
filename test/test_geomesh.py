import unittest
from unittest.mock import MagicMock, patch
from geoserver.geomesh import Geomesh

class TestGeomesh(unittest.TestCase):
    def setUp(self):
        self.geomesh = Geomesh(database_dir='test_db')

    def test_get_data(self):
        result = self.geomesh.get_data('test_dataset', year=2023)
        self.assertIsInstance(result, list)

    @patch('geo_infer_space.repo.osc_geo_h3grid_srv.geoserver.geomesh.shape.Shape')
    def test_filter(self, mock_shape):
        mock_shape_instance = mock_shape.return_value
        mock_shape_instance.get_h3_in_shape.return_value = ['test_cell']
        result = self.geomesh.filter('test_shapefile', resolution=8)
        self.assertEqual(result, ['test_cell']) 