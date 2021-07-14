from geom2d.point import Point
from utils.pairs import make_pairs
from geom2d.segment import Segment
import operator
from functools import reduce
from geom2d.vectors import make_vector_btw
from geom2d.nums import are_close_enough
import math

class Polygon:
    def __init__(self,vertices: [Point]):
        if len(vertices) < 3:
            raise ValueError('Need 3 or more vertices')
        self.vertices=vertices

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Polygon):
            return False
        return self.vertices==other.vertices

    def sides(self):
        vertex_pairs = make_pairs(self.vertices)
        return[Segment(pair[0], pair[1])
               for pair in vertex_pairs]

    def contains_point(self, point):
        if point in self.vertices:
            return True
        vecs=[make_vector_btw(point,vertex)
              for vertex in self.vertices]
        pair_vecs=make_pairs(vecs)
        sum = reduce(operator.add,[v1.signed_angle(v2) for v1, v2 in pair_vecs])
        return are_close_enough(sum,2*math.pi)

    @property
    def centroid(self):
        length = len(self.vertices)
        sum = reduce(operator.add, self.vertices)
        return Point(sum.x/length, sum.y/length)
