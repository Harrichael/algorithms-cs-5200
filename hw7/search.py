
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
    def __init__(self, initial_set, neighbors, is_goal, pre_explored=None):
        self.goal = None
        self.explored = set()
        if pre_explored:
            self.explored.update(pre_explored)
        self.parents = {}
        frontier = deque()
        for initial_vertex in initial_set:
            self.parents[initial_vertex] = None
            frontier.append(initial_vertex)

        while True:
            if not frontier:
                break
            select_node = frontier.popleft()
            self.explored.add(select_node)

            if is_goal(select_node):
                self.goal = select_node
                break

            for new_node in [n for n in neighbors(select_node) if n not in self.explored]:
                self.parents[new_node] = select_node
                frontier.append(new_node)

"""
Depth First Graph Search
"""
class DFGS(SearchSolver):
    def __init__(self, initial_set, neighbors, is_goal, pre_explored=None):
        self.goal = None
        self.explored = set()
        if pre_explored:
            self.explored.update(pre_explored)
        frontier = []
        self.parents = {}
        for initial_vertex in initial_set:
            self.parents[initial_vertex] = None
            frontier.append(initial_vertex)

        while True:
            if not frontier:
                break
            select_node = frontier.pop()
            self.explored.add(select_node)

            if is_goal(select_node):
                self.goal = select_node
                break

            for new_node in [n for n in neighbors(select_node) if n not in self.explored]:
                self.parents[new_node] = select_node
                frontier.append(new_node)

