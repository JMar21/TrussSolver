import math


def are_close_enough(a, b, tolerance=1e-10):
    return math.fabs(a-b) < tolerance
