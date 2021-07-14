from geom2d.rect import Rect
from geom2d.point import Point
from geom2d.size import Size

def make_rect_contains(points):
    if not points:
        raise ValueError('Expected one or more points')
    first = points[0]
    min_x, max_x = first.x, first.x
    min_y, max_y = first.y, first.y
    for point in points[1:]:
        min_x, max_x = min(min_x, point.x), max(max_x, point.x)
        min_y, max_y = min(min_x, point.y), max(max_y, point.y)
    return Rect(Point(min_x, min_y),Size(max_x-min_x, max_y-min_y))

def make_rect_with_margin(points, margin):
    rect = make_rect_contains(points)
    return Rect(Point(rect.origin.x-margin,rect.origin.y-margin),
                Size(2*margin + rect.size.width, 2*margin + rect.size.height))
def make_rect_centered(center, width, height):
    origin = Point(center.x-width/2, center.y -height/2)
    return Rect(origin, Size(width, height))