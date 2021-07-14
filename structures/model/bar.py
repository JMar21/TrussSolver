from geom2d import Segment
from .node import StrNode
from eqs.matrix import Matrix
class StrBar:

    def __init__(self, id, start_node, end_node, area, E):
        self.id = id
        self.start_node = start_node
        self.end_node = end_node
        self.area = area
        self.E = E

    def global_stiffness_matrix(self) -> Matrix:
        direct = self.geometry.dir_vec
        eal = self.E * self.area / self.length
        c = direct.cos()
        s = direct.sin()
        c2_eal = (c ** 2) * eal
        s2_eal = (s ** 2) * eal
        sc_eal = (s * c) * eal
        return Matrix(4, 4).set_data([
            c2_eal, sc_eal, -c2_eal, -sc_eal,
            sc_eal, s2_eal, -sc_eal, -s2_eal,
            -c2_eal, -sc_eal, c2_eal, sc_eal,
            -sc_eal, -s2_eal, sc_eal, s2_eal
        ])
    @property
    def geometry(self):
        return Segment(self.start_node.position, self.end_node.position)

    @property
    def length(self):
        return self.geometry.length