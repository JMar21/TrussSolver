from geom2d.point import Point
from geom2d.polygon import Polygon

def make_polygon_from_coords(coords):
    if len(coords) % 2 !=0:
        raise ValueError('Need even number of coords')
    indices = range(0,len(coords),2)
    return Polygon([Point(coords[i], coords[i+1]) for i in indices])