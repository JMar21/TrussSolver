import math
from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.nums import are_close_enough

class Circle:
    def __init__(self, center: Point, radius):
        self.center=center
        self.radius=radius

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Circle):
            return False
        return self.center == other.center and are_close_enough(self.radius, other.radius)

    def __str__(self):
        return f'circle c ={self.center}, r ={self.radius}'
    def contains_point(self, point: Point):
        return self.center.distance_to_point(point) < self.radius

    def convert_to_polygon(self,divs):
        angle_diff = 2 * math.pi/divs
        return Polygon([self.__point_at_angle(angle_diff*i) for i in range(divs)])

    def __point_at_angle(self, angle):
        return Point(self.center.x+ self.radius * math.cos(angle), self.center.y + self.radius * math.sin(angle))


    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def circumference(self):
        return math.pi * 2 * self.radius
