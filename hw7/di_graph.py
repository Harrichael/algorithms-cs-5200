
from collections import defaultdict

class Graph:
    def __init__(self, edges=None):
        self.edge_lists = defaultdict(list)
        if edges:
            self.add_edges(edges)

    @property
    def vertices(self):
        return list(self.edge_lists.keys())

    def add_edges(self, edges):
        for v1, v2 in edges:
            if v2 not in self.edge_lists[v1]: # Edges are symetric
                self.edge_lists[v1].append(v2)

    def get_neighbor_func(self):
        def neighbors(v):
            return self.edge_lists[v]
        return neighbors


