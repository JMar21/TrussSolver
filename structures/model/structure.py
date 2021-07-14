from functools import reduce
from .node import StrNode
from .bar import StrBar
from eqs import Matrix, solve_cholesky
from eqs.vector import Vector as EqVector
from geom2d import Vector
from structures.solution.bar import StrBarSolution
from structures.solution.node import StrNodeSolution
from structures.solution.structure import StructureSolution

class Structure:
    __DOF_PER_NODE = 2
    def __init__(self, nodes: [StrNode], bars: [StrBar]):
        self.__bars = bars
        self.__nodes = nodes
        self.__dofs_dict = None
        self.__sys_mat: Matrix = None
        self.__sys_vec: EqVector = None
        self.__global_disp: EqVector = None

    def solve_structure(self):
        self.__assign_dof()
        self.__solve_sys_of_eq()
        return self.__make_structure_solution()

    def __solve_sys_of_eq(self):
        size = self.node_count * self.__DOF_PER_NODE
        self.__assemble_sys_mat(size)
        self.__assemble_sys_vec(size)
        self.__apply_ext_constraints()
        self.__global_disp = solve_cholesky(self.__sys_mat, self.__sys_vec)

    def __assign_dof(self):
        self.__dofs_dict = {}
        for i, node in enumerate(self.__nodes):
            self.__dofs_dict[node.id] = (2 * i, 2*i +1)

    def __assemble_sys_mat(self, size):
        matrix = Matrix(size, size)
        for bar in self.__bars:
            bar_matrix = bar.global_stiffness_matrix()
            dofs = self.__bar_dofs(bar)
            for row, row_dof in enumerate(dofs):
                for col, col_dof in enumerate(dofs):
                    matrix.add_to_value(bar_matrix.value_at(row, col),\
                                        row_dof, col_dof)
        self.__sys_mat = matrix

    def __bar_dofs(self, bar: StrBar):
        start_dofs = self.__dofs_dict[bar.start_node.id]
        end_dofs = self.__dofs_dict[bar.end_node.id]
        return start_dofs + end_dofs

    def __assemble_sys_vec(self, size):
        vector = EqVector(size)
        for node in self.__nodes:
            net_load = node.net_load
            (dof_x, dof_y) = self.__dofs_dict[node.id]
            vector.add_to_value(net_load.u, dof_x)
            vector.add_to_value(net_load.v, dof_y)

        self.__sys_vec = vector

    def __apply_ext_constraints(self):
        for node in self.__nodes:
            (dof_x, dof_y) = self.__dofs_dict[node.id]

            if node.dx_constrained:
                self.__sys_mat.set_identity_row(dof_x)
                self.__sys_mat.set_identity_col(dof_x)
                self.__sys_vec.set_value(0, dof_x)

            if node.dy_constrained:
                self.__sys_mat.set_identity_row(dof_y)
                self.__sys_mat.set_identity_col(dof_y)
                self.__sys_vec.set_value(0, dof_y)

    def __make_structure_solution(self) -> StructureSolution:
        nodes = [self.__node_to_solution(node)
                 for node in self.__nodes]
        nodes_dict = {}
        for node in nodes:
            nodes_dict[node.id] = node
        bars = [StrBarSolution(bar, nodes_dict[bar.start_node.id], nodes_dict[bar.end_node.id])
                for bar in self.__bars]
        return StructureSolution(nodes, bars)

    def __node_to_solution(self, node) -> StrNodeSolution:
        (dof_x, dof_y) = self.__dofs_dict[node.id]
        disp = Vector(self.__global_disp.value_at(dof_x), self.__global_disp.value_at((dof_y)))
        return StrNodeSolution(node, disp)
    @property
    def node_count(self):
        return len(self.__nodes)

    @property
    def bar_count(self):
        return len(self.__bars)

    @property
    def load_count(self):
        return reduce(lambda count, node: count + node.loads_count, self.__nodes, 0)
