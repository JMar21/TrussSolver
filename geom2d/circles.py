from geom2d.point import Point
from geom2d.circle import Circle
from geom2d.segment import Segment

def make_circle_three_points(a,b,c):
    bisec1 = Segment(a,b).bisector
    bisec2 = Segment(b,c).bisector
    center = bisec1.intersection_with(bisec2)
    radius = center.distance_to_point(a)
    return Circle(center, radius)
