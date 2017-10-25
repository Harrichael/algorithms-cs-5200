
from collections import Counter

from di_graph import Graph
from search import BFGS, DFGS

graph_edges = [
	('r', 'u'),
        ('r', 'y'),
        ('u', 'y'),
        ('y', 'q'),
        ('q', 's'),
        ('q', 'w'),
        ('q', 't'),
        ('s', 'v'),
        ('v', 'w'),
        ('w', 's'),
        ('t', 'x'),
        ('t', 'y'),
        ('x', 'z'),
        ('z', 'x'),
    ]

def print_dfs_trace(graph):
    node_discovery = {}
    node_exits = {}
    parents = {}

    neighbors = lambda n: list(sorted(graph.get_neighbor_func()(n), reverse=True))

    counter = 1
    def check_node(node):
        nonlocal counter

        for n in neighbors(node):
            if n not in parents:
                parents[n] = node

        if node not in parents:
            parents[node] = None
            node_discovery[node] = counter
            counter += 1
        elif parents[node] in node_discovery and node_discovery[parents[node]] == counter - 1:
            node_discovery[node] = counter
            counter += 1
        else:
            curr = [n for n, c in node_discovery.items() if c == counter - 1][0]
            while curr != parents[node] and curr is not None:
                node_exits[curr] = counter
                counter += 1
                curr = parents[curr]
            node_discovery[node] = counter
            counter += 1

        return False

    searcher = DFGS('q', neighbors, check_node)
    curr = [n for n, c in node_discovery.items() if c == counter - 1][0]
    while curr is not None:
        node_exits[curr] = counter
        counter += 1
        curr = parents[curr]
    DFGS('r', neighbors, check_node, searcher.explored)
    curr = [n for n, c in node_discovery.items() if c == counter - 1][0]
    while curr is not None:
        node_exits[curr] = counter
        counter += 1
        curr = parents[curr]

    for node in sorted(node_discovery.keys()):
        print(node, node_discovery[node], node_exits[node])

if __name__ == '__main__':
    graph = Graph(graph_edges)
    print_dfs_trace(graph)

