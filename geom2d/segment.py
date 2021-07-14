from geom2d.point import Point
from geom2d.vectors import make_vector_btw, make_versor_btw, Vector
from geom2d import tparam
from geom2d.line import Line

class Segment:
    def __init__(self, start: Point , end: Point):
        self.start = start
        self.end = end

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other,Segment):
            return False
        if other.start == self.start and other.end == self.end:
            return True

        return False

    def __str__(self):
        return f'segment from {self.start} to {self.end}'
    def pointAt(self, t):
        tparam.ensure_valid(t)
        return self.start.displacedBy(self.dir_vec, t)

    def closestPoint(self, point):
        temp = make_vector_btw(self.start, point)
        d = self.dir_vers
        projected = temp.projection_to(d)
        if projected < 0:
            return self.start
        if projected > self.length:
            return self.end
        return self.start.displacedBy(d, projected)

    def distanceTo(self, point):
        return point.distance_to_point(self.closestPoint(point))

    def intersection_with(self, other):
        d1, d2 = self.dir_vec, other.dir_vec
        if d1.is_parallel_to(d2):
            return None
        cross=d1.cross(d2)
        delta = other.start - self.start
        t1 = (delta.u * d2.v - delta.v * d2.u) / cross
        t2 = (delta.u * d1.v - delta.v * d1.u) / cross
        if tparam.is_valid(t1) and tparam.is_valid(t2):
            return self.pointAt(t1)
        else:
            return None
    
    @property
    def bisector(self):
        return Line(self.midpoint,self.norm_vers)

    @property
    def midpoint(self):
        return self.pointAt(tparam.MID)

    @property
    def dir_vec(self):
        return make_vector_btw(self.start, self.end)

    @property
    def dir_vers(self):
        return make_versor_btw(self.start, self.end)

    @property
    def norm_vers(self):
        return self.dir_vers.perpVector()

    @property
    def length(self):
        return self.start.distance_to_point(self.end)
