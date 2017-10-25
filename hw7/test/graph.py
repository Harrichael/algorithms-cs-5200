
from graph import Graph, BFGS, DFGS

graph1_edges = [
        (13, 0),
        (13, 6),
        (15, 0),
        (15, 3),
        (5, 6),
        (4, 13),
        (5, 0),
        (11, 3),
        (9, 1),
        (5, 14),
        (5, 7),
        (13, 6),
        (12, 14),
        (1, 6),
        (14, 4),
        (2, 0),
        (13, 6),
        (8, 1),
        (0, 7),
        (12, 2),
        (3, 1),
        (4, 1),
        (4, 5),
        (9, 5),
        (6, 15),
        (14, 14),
        (9, 13),
        (1, 7),
        (11, 0),
        (14, 15),
        (4, 2),
        (5, 0),
        (7, 8),
        (3, 7),
        (5, 5),
        (7, 2),
        (6, 9),
        (10, 7),
        (15, 15),
        (4, 12),
        (9, 6),
        (15, 10),
        (10, 7),
        (9, 11),
        (0, 9),
        (11, 14),
        (10, 5),
        (2, 15),
    ]

graph2_edges = [
        (3, 1),
        (2, 9),
        (8, 9),
        (5, 3),
        (5, 8),
        (3, 1),
        (1, 9),
        (2, 6),
        (7, 6),
        (8, 5),
        (4, 4),
        (4, 6),
        (6, 6),
        (1, 3),
        (5, 9),
        (11, 14),
        (15, 17),
        (19, 18),
        (14, 17),
        (19, 17),
        (14, 10),
        (10, 19),
        (19, 15),
        (10, 12),
        (13, 11),
        (15, 16),
        (11, 16),
        (16, 14),
        (12, 15),
        (11, 18),
    ]

def test_graph_starts(graph, starts):
    for start in starts:
        print()
        print('Testing start vertex {}'.format(start))
        test_graph(graph, start)

def test_graph(graph, start):
    for end in graph.vertices:
        bf_search = BFGS(start, graph.get_neighbor_func(), lambda n: n == end)
        df_search = DFGS(start, graph.get_neighbor_func(), lambda n: n == end)

        print('Dest =', end, bf_search.path, ' '*(30 - len(str(bf_search.path))), df_search.path)

def main():
    print('Testing Graph 1')
    graph1 = Graph(graph1_edges)
    test_graph_starts(graph1, [1, 5, 14])

    print()
    print('Testing Graph 2')
    graph2 = Graph(graph2_edges)
    test_graph_starts(graph2, [1, 11, 19])

if __name__ == '__main__':
    main()

