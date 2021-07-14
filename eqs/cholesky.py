import math

from eqs.matrix import Matrix
from eqs.vector import Vector

def solve_cholesky(sys_mat: Matrix, sys_vec: Vector):
    validate_system(sys_mat, sys_vec)
    l_matrix = lower_decomp(sys_mat)
    l_solution = solve_lower_sys(l_matrix, sys_vec)
    return solve_upper_sys(l_matrix, l_solution)

def validate_system(sys_mat, sys_vec):
    if sys_mat.cols_count != sys_vec.length:
        raise ValueError('incompatible sizes')
    if not sys_mat.is_square:
        raise ValueError('matrix must be square')

def lower_decomp(sys_mat: Matrix):
    size = sys_mat.rows_count
    l_mat = Matrix(size, size)
    for i in range(size):
        sq_sum =0
        for j in range(i+1):
            m_ij = sys_mat.value_at(i, j)
            if i == j:
                diag_val = math.sqrt(m_ij - sq_sum)
                l_mat.set_value(diag_val, i, j)
            else:
                non_diag_sum = 0
                for k in range(j):
                    l_ik = l_mat.value_at(i, k)
                    l_jk = l_mat.value_at(j, k)
                    non_diag_sum += l_ik * l_jk
                l_jj = l_mat.value_at(j, j)
                non_diag_val = (m_ij - non_diag_sum)/l_jj
                sq_sum += non_diag_val * non_diag_val
                l_mat.set_value(non_diag_val, i, j)
    return l_mat

def solve_lower_sys(l_mat: Matrix, vector: Vector):
    size= vector.length
    sol = Vector(size)
    for i in range(size):
        _sum = 0.0
        for j in range(i):
            l_ij = l_mat.value_at(i,j)
            y_j = sol.value_at(j)
            _sum+=l_ij * y_j

        b_i = vector.value_at(i)
        l_ii = l_mat.value_at(i, i)
        sol_val = (b_i - _sum)/l_ii
        sol.set_value(sol_val, i)
    return sol

def solve_upper_sys(up_mat: Matrix, vector: Vector):
    size = vector.length
    last_index = size -1
    sol = Vector(size)
    for i in range(last_index, -1, -1):
        _sum = 0.0
        for j in range(i+1, size):
            u_ij = up_mat.value_at_transposed(i, j)
            x_j = sol.value_at(j)
            _sum += u_ij * x_j
        y_i = vector.value_at(i)
        u_ii = up_mat.value_at_transposed(i, i)
        sol_val = (y_i - _sum)/u_ii
        sol.set_value(sol_val, i)
    return sol