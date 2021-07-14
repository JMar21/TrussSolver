import math
from geom2d.vector import Vector
from geom2d import nums
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_point(self, other):
        dx = other.x-self.x
        dy = other.y-self.y
        return math.sqrt(dx**2+dy**2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self,other):
        if self is other:
            return True
        if not isinstance(other, Point):
            return False
        return nums.are_close_enough(self.x, other.x) and nums.are_close_enough(self.y, other.y)

    def displacedBy(self, dist: Vector, times=1):
        scaled_disp = dist.scaledBy(times)
        return Point(self.x + scaled_disp.u, self.y + scaled_disp.v)

    def to_formatted_str(self, decimals):
        x=round(self.x, decimals)
        y=round(self.y, decimals)
        return f'({x}, {y})'
    
    def __str__(self):
        return f'({self.x}, {self.y})'


