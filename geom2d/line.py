from geom2d.point import Point
from geom2d.vector import Vector
from geom2d.vectors import make_vector_btw

class Line:
    def __init__(self, base: Point, dir: Vector):
        self.base = base
        self.dir = dir

    def is_parallel_to(self, other):
        return self.dir.is_parallel_to(other.dir)

    def is_perp_to(self, other):
        return self.dir.is_perpendicular_to(other.dir)

    def perp_thru(self,):
        return Line(self.base, self.dir.perpVector())

    def par_thru(self):
        return Line(self.base, self.dir)

    def intersection_with(self, other):
        if self.is_parallel_to(other):
            return None
        d1 = self.dir
        d2 = other.dir
        cross = d1.cross(d2)
        delta = make_vector_btw(self.base, other.base)
        t=(delta.u * d2.v - delta.v * d2.u)/cross
        return self.base.displacedBy(d1, t)
