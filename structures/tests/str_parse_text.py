import unittest
import pkg_resources as res
from structures.parse import parse_structure
from geom2d import Point

class TestParseStructure(unittest.TestCase):
    def setUp(self):
        str_bytes = res.resource_string(__name__, 'test_str.txt')
        str_string = str_bytes.decode("utf-8")
        self.structure = parse_structure(str_string)

    def test_parse_nodes_count(self):
        self.assertEqual(3, self.structure.node_count)

    def test_parse_nodes(self):
        nodes = self.structure._Structure__nodes
        self.assertEqual(Point(0,0),nodes[0].position)
        self.assertEqual(Point(200,150), nodes[1].position)
        self.assertEqual(Point(400,0),nodes[2].position)

    def test_parse_node_constraints(self):
        nodes = self.structure._Structure__nodes
        self.assertTrue(nodes[0].dx_constrained)
        self.assertTrue(nodes[0].dy_constrained)
        self.assertFalse(nodes[1].dx_constrained)
        self.assertFalse(nodes[1].dy_constrained)
        self.assertFalse(nodes[2].dx_constrained)
        self.assertTrue(nodes[2].dy_constrained)