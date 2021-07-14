from geom2d import nums
import math
class Vector:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __add__(self, other):
        return Vector(self.u + other.u, self.v + other.v)

    def __sub__(self, other):
        return Vector(self.u - other.u, self.v - other.v)
    
    def __eq__(self,other):
        if self is other:
            return True
        if not isinstance(other, Vector):
            return False
        return nums.are_close_enough(self.u, other.u) and nums.are_close_enough(self.v, other.v)

    def scaledBy(self, scaleF):
        return Vector(scaleF* self.u , scaleF * self.v)

    def dot(self, other):
        return self.u * other.u + self.v * other.v

    def cross(self, other):
        return self.u * other.v - self.v * other.u

    def projection_to(self, other):
        return self.dot(other.normalized())

    def normalized(self):
        return self.scaledBy(1.0 / self.norm)

    def with_length(self, length):
        return self.normalized().scaledBy(length)

    def is_parallel_to(self, other):
        return nums.are_close_enough(self.cross(other), 0)

    def is_perpendicular_to(self, other):
        return nums.are_close_enough(self.dot(other), 0)

    def angle_value(self, other):
        dot_prod = self.dot(other)
        denom = self.norm * other.norm
        return math.acos(dot_prod/denom)

    def signed_angle(self, other):
        angleVal = self.angle_value(other)
        crossProd = self.cross(other)
        return math.copysign(angleVal, crossProd)

    def sin(self):
        return self.v/self.norm

    def cos(self):
        return self.u/self.norm

    def rotated_by_rads(self, rads):
        return Vector(self.u * math.cos(rads) - self.v * math.sin(rads), self.u * math.sin(rads) + self.v * math.cos(rads))

    def perpVector(self):
        return Vector(-self.v, self.u)

    def antiparallel(self):
        return Vector(-self.u, -self.v)

    def to_formatted_str(self, decimals):
        u=round(self.u, decimals)
        v=round(self.v, decimals)
        norm = round(self.norm, decimals)
        return f'({u}, {v}) with norm {norm}'
    @property
    def norm(self):
        return math.sqrt(self.u**2 + self.v**2)

    @property
    def is_normal(self):
        return nums.are_close_enough(self.norm , 1, 1e-10)
