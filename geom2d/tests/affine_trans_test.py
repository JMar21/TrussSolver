import unittest
from geom2d.point import Point
from geom2d.affine_trans import  AffineTransform

class TestAffineTrans(unittest.TestCase):
    point = Point(2,3)
    scale = AffineTransform(2,5)
    trans = AffineTransform(1, 1, 10, 15)
    shear = AffineTransform(1, 1, 0, 0, 3, 4)

    def test_scale(self):
        actual = self.scale.apply_to_point(self.point)
        expected = Point(4, 15)
        self.assertEqual(actual, expected)

    def test_shear(self):
        actual = self.shear.apply_to_point(self.point)
        expected = Point(11, 11)
        self.assertEqual(actual, expected)

    def test_trans(self):
        actual = self.trans.apply_to_point(self.point)
        expected = Point( 12, 18)
        self.assertEqual(actual, expected)

    def test_multi_scale_then_trans(self):
        expected = AffineTransform(2,5,10,15)
        actual = self.scale.multiple_trans(self.trans)
        self.assertEqual(expected, actual)

    def test_multi_trans_then_scale(self):
        expected = AffineTransform(2,5,20,75)
        actual = self.trans.multiple_trans(self.scale)
        self.assertEqual(expected, actual)

    def test_inverse(self):
        trans = AffineTransform(1, 2, 3, 4, 5, 6)
        expected = AffineTransform()
        actual = trans.multiple_trans(trans.inverse())
        self.assertEqual(expected, actual)

