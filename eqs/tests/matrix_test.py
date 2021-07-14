import unittest
from eqs.matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_square_matrix(self):
        self.assertTrue(Matrix(2,2).is_square)

    def test_not_square(self):
        self.assertFalse(Matrix(2,3).is_square)

    def test_default_zero_values(self):
        matrix = Matrix(2, 2)
        self.assertEqual(0.0, matrix.value_at(0, 1))

    def test_set_get_value(self):
        value = 10.0
        matrix = Matrix(2, 2).set_value(value, 0, 1)
        self.assertEqual(value, matrix.value_at(0, 1))

    def test_add_to_value(self):
        expected = [1, 12, 3, 4]
        matrix = Matrix(2, 2).set_data([1, 2, 3, 4]).add_to_value(10, 0, 1)
        self.assert_matrix_has_data(matrix, expected)

    def assert_matrix_has_data(self, matrix, data):
        for row in range(matrix.rows_count):
            offset = matrix.cols_count * row
            for col in range(matrix.cols_count):
                self.assertEqual(data[offset + col], matrix.value_at(row,col))

    def test_set_data(self):
        data=[1,2,3,4,5,6]
        matrix = Matrix(2,3).set_data(data)
        self.assert_matrix_has_data(matrix, data)

    def test_set_identity_row(self):
        expected = [1, 0, 4, 5]
        actual = Matrix(2,2).set_data([2, 3, 4, 5]).set_identity_row(0)
        self.assert_matrix_has_data(actual, expected)

    def test_set_identity_col(self):
        expected = [2, 0, 4, 1]
        actual = Matrix(2,2).set_data([2, 3, 4, 5]).set_identity_col(1)
        self.assert_matrix_has_data(actual, expected)

    def test_scaling(self):
        expected = [2, 4, 6, 8, 10 ,12]
        actual = Matrix(2,3).set_data([1, 2, 3, 4, 5, 6]).scaledBy(2)
        self.assert_matrix_has_data(actual, expected)