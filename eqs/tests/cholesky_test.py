import unittest
from eqs.cholesky import lower_decomp, solve_lower_sys, solve_upper_sys, solve_cholesky
from eqs.matrix import Matrix
from eqs.vector import Vector

class TestCholesky(unittest.TestCase):
    sys_mat = Matrix(4,4).set_data([4, -2, 4, 2, -2, 10, -2, -7,
                                     4, -2, 8, 4, 2, -7, 4, 7])
    l_mat = Matrix(4,4).set_data([2, 0, 0, 0, -1, 3, 0, 0,
                                   2, 0, 2, 0, 1, -2, 1, 1])
    sys_vec = Vector(4).set_data([20, -16, 40, 28])
    l_sol = Vector(4).set_data([10, -2, 10, 4])
    sol = Vector(4).set_data([1, 2, 3, 4])
    def test_lower_mat_decomp(self):
        actual = lower_decomp(self.sys_mat)
        self.assertEqual(self.l_mat, actual)

    def test_lower_sys_sol(self):
        actual = solve_lower_sys(self.l_mat, self.sys_vec)
        self.assertEqual(self.l_sol, actual)

    def test_upper_sys_sol(self):
        actual = solve_upper_sys(self.l_mat, self.l_sol)
        self.assertEqual(self.sol, actual)

    def test_solve_sys(self):
        actual = solve_cholesky(self.sys_mat, self.sys_vec)
        self.assertEqual(self.sol, actual)

