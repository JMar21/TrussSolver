from structures.model.bar import StrBar
from .node import StrNodeSolution
from geom2d import Segment, make_vector_btw

class StrBarSolution:
    def __init__(self, og_bar: StrBar, start_node: StrNodeSolution, end_node:StrNodeSolution):
        if og_bar.start_node.id != start_node.id:
            raise ValueError('Wrong start node')
        if og_bar.end_node.id != end_node.id:
            raise ValueError('Wrong end node')

        self.__original_bar = og_bar
        self.start_node = start_node
        self.end_node = end_node

    def force_in_node(self, node: StrNodeSolution):
        if node is self.start_node:
            return make_vector_btw(self.end_node.displaced_pos, self.start_node.displaced_pos).\
                with_length(self.internal_force_value)
        elif node is self.end_node:
            return make_vector_btw(self.start_node.displaced_pos, self.end_node.displaced_pos).\
                with_length(self.internal_force_value)
        raise ValueError(f'Bar {self.id} does not contain node {node.id}')

    def has_node(self, node: StrNodeSolution):
        return node is self.start_node or node is self.end_node

    def final_geometry_disp(self, scale):
        return Segment(self.start_node.displaced_pos_scaled(scale), self.end_node.displaced_pos_scaled(scale))
    
    @property
    def id(self):
        return self.__original_bar.id

    @property
    def area(self):
        return self.__original_bar.area

    @property
    def E(self):
        return self.__original_bar.E

    @property
    def original_geometry(self):
        return self.__original_bar.geometry

    @property
    def final_geometry(self):
        return Segment(self.start_node.displaced_pos, self.end_node.displaced_pos)

    @property
    def final_length(self):
        return self.final_geometry.length

    @property
    def original_length(self):
        return self.original_geometry.length

    @property
    def elongation(self):
        return self.final_length-self.original_length

    @property
    def strain(self):
        return self.elongation / self.original_length

    @property
    def stress(self):
        return self.E * self.strain

    @property
    def internal_force_value(self):
        return self.stress * self.area


