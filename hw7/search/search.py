
from itertools import count
from collections import deque, defaultdict

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
                self.edge_lists[v2].append(v1)

    def get_neighbor_func(self):
        def neighbors(v):
            return self.edge_lists[v]
        return neighbors

"""
Base Search Solver
"""
class SearchSolver:
    @property
    def path(self):
        path = []
        curr = self.goal
        while curr is not None:
            path.append(curr)
            curr = self.parents[curr]

        return list(reversed(path))

"""
Breadth First Graph Search
"""
class BFGS(SearchSolver):
    def __init__(self, initial_vertex, neighbors, is_goal):
        self.goal = None
        self.parents = {initial_vertex: None}
        explored = set()
        frontier = deque()
        frontier.append(initial_vertex)
        while True:
            if not frontier:
                break
            select_node = frontier.popleft()
            explored.add(select_node)

            if is_goal(select_node):
                self.goal = select_node
                break

            for new_node in [n for n in neighbors(select_node) if n not in explored]:
                self.parents[new_node] = select_node
                frontier.append(new_node)

"""
Depth First Graph Search
"""
class DFGS(SearchSolver):
    def __init__(self, initial_vertex, neighbors, is_goal):
        self.goal = None
        self.parents = {initial_vertex: None}
        explored = set()
        frontier = []
        frontier.append(initial_vertex)
        while True:
            if not frontier:
                break
            select_node = frontier.pop()
            explored.add(select_node)

            if is_goal(select_node):
                self.goal = select_node
                break

            for new_node in [n for n in neighbors(select_node) if n not in explored]:
                self.parents[new_node] = select_node
                frontier.append(new_node)

