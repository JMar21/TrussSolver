from geom2d.point import Point
from geom2d.vector import Vector


def make_vector_btw(p,q):
    return q-p


def make_versor(u, v):
    return Vector(u, v).normalized()


def make_versor_btw(p, q):
    return make_vector_btw(p, q).normalized()