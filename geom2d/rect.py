from geom2d.point import Point
from geom2d.size import Size
from geom2d.open_interval import OpenInterval
from geom2d.polygon import Polygon

class Rect:
    def __init__(self, origin, size):
        self.origin = origin
        self.size= size

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Rect):
            return False
        return self.origin == other.origin and self.size == other.size
    
    def contains_point(self, point):
        if self.left<point.x<self.right and self.bottom<point.y<self.top:
            return True

    def intersection_with(self, other):
        h_overlap = self.__h_overlap_with(other)
        if h_overlap is None:
            return None
        v_overlap = self.__v_overlap_with(other)
        if v_overlap is None:
            return None
        return Rect(Point(h_overlap.start, v_overlap.start), Size(h_overlap.length, v_overlap.length))

    def __h_overlap_with(self, other):
        self_int = OpenInterval(self.left, self.right)
        other_int = OpenInterval(other.left, other.right)
        return self_int.compute_overlap(other_int)

    def __v_overlap_with(self, other):
        self_int = OpenInterval(self.bottom, self.top)
        other_int = OpenInterval(other.bottom, other.top)
        return self_int.compute_overlap(other_int)

    def to_polygon(self):
        return Polygon([self.origin, Point(self.right, self.bottom), Point(self.right, self.top),
                       Point(self.left, self.top)])
    @property
    def left(self):
        return self.origin.x

    @property
    def right(self):
        return self.origin.x + self.size.width

    @property
    def bottom(self):
        return self.origin.y

    @property
    def top(self):
        return self.origin.y + self.size.height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perim(self):
        return 2*self.width + 2*self.height