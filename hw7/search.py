
from collections import deque

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

