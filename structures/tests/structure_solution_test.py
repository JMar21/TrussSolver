import unittest
from unittest.mock import patch, Mock
from geom2d import Point
from structures.solution.node import StrNodeSolution
from structures.solution.structure import StructureSolution

class TestStructureSolution(unittest.TestCase):
    p_1  = Point(2,3)
    p_2 = Point(5,1)
    def setUp(self):
        self.n_1 = Mock(spec=StrNodeSolution)
        self.n_1.displaced_pos_scaled.return_value = self.p_1
        self.n_2 = Mock(spec=StrNodeSolution)
        self.n_2.displaced_pos_scaled.return_value = self.p_2
    def test_node_displaced_scaled(self):
        sol = StructureSolution([self.n_1, self.n_2], [])
        sol.boundary_rect(margin=10, scale=4)
        self.n_1.displaced_pos_scaled.assert_called_once_with(4)
        self.n_2.displaced_pos_scaled.assert_called_once_with(4)

    @patch('structures.solution.structure.make_rect_with_margin')
    def test_make_rect_called(self, make_rect_mock):
        sol = StructureSolution([self.n_1, self.n_2], [])
        sol.boundary_rect(margin=10, scale=4)
        make_rect_mock.assert_called_once_with([self.p_1, self.p_2], 10)