from .bar import StrBarSolution
from .node import StrNodeSolution
from geom2d import make_rect_with_margin, Vector
import operator
from functools import reduce

class StructureSolution:
    def __init__(self, nodes: [StrNodeSolution], bars: [StrBarSolution]):
        self.nodes = nodes
        self.bars = bars

    def boundary_rect(self, margin, scale=1):
        d_pos = [node.displaced_pos_scaled(scale)
                 for node in self.nodes]
        return make_rect_with_margin(d_pos, margin)

    def reaction_for_node(self, node: StrNodeSolution):
        if not node.is_constrained:
            return Vector(0,0)

        forces = [bar.force_in_node(node)
                  for bar in self.bars if bar.has_node(node)]
        if node.is_loaded:
            forces.append(node.net_load.antiparallel())

        return reduce(operator.add, forces)
