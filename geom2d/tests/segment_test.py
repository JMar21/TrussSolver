import math
import unittest
from geom2d.point import Point
from geom2d.segment import Segment
from geom2d import tparam

class TestSegment(unittest.TestCase):
    start = Point(400,0)
    end = Point(0,400)
    segment = Segment(start,end)

    def test_length(self):
        expected = 400 * math.sqrt(2)
        actual = self.segment.length
        self.assertAlmostEqual(expected, actual)

    def test_point_at(self):
        t=tparam.make(0.25)
        expected = Point(300,100)
        actual = self.segment.pointAt(t)
        self.assertEqual(expected, actual)

    def test_midpoint(self):
        expected = Point(200,200)
        actual = self.segment.midpoint
        self.assertEqual(expected, actual)

    def test_point_at_wrong_t(self):
        self.assertRaises(tparam.TParamError, self.segment.pointAt, 10)

    def test_closest_point_is_start(self):
        p = Point(500, 20)
        expected = self.segment.start
        actual = self.segment.closestPoint(p)
        self.assertEqual(expected, actual)

    def test_closest_point_is_end(self):
        q = Point(20,500)
        expected = self.segment.end
        actual = self.segment.closestPoint(q)
        self.assertEqual(expected, actual)

    def test_closest_point_is_midpoint(self):
        r = Point(250,250)
        expected = Point(200,200)
        actual = self.segment.closestPoint(r)
        self.assertEqual(expected, actual)

    def test_parallel_no_intersection(self):
        other = Segment(Point(200,0), Point(0,200))
        actual = self.segment.intersection_with(other)
        self.assertIsNone(actual)

    def test_segments_intersect(self):
        other = Segment(Point(0,0), Point(400,400))
        expected = Point(200,200)
        actual = self.segment.intersection_with(other)
        self.assertEqual(expected,actual)
