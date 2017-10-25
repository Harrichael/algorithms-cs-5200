
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


