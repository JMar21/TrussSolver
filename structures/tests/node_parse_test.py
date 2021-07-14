import unittest

from geom2d import Point
from structures.parse.node_parse import parse_node

class TestParseNode(unittest.TestCase):
    node_str = '1: (25.0, 45.0)    (xy)'
    node = parse_node(node_str)
    def test_parse_id(self):
        self.assertEqual(1, self.node.id)
    def test_parse_pos(self):
        expected = Point(25.0, 45.0)
        self.assertEqual(expected, self.node.position)
    def test_parse_dx_ext_cons(self):
        self.assertTrue(self.node.dx_constrained)
    def test_parse_dy_ext_cons(self):
        self.assertTrue(self.node.dy_constrained)
