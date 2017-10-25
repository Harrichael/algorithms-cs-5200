
from graph import Graph
from search import BFGS

def color_bipartite(nodes, edges):
    graph = Graph(edges)
    node_color = {}

    neighbors = graph.get_neighbor_func()
    
    def check_node(node):
        if node not in node_color:
            node_color[node] = True

        color = not node_color[node]
        for neighbor in neighbors(node):
            if neighbor not in node_color:
                node_color[neighbor] = color
            elif node_color[neighbor] != color:
                raise ValueError('Not Bipartite')

        return False

    try:
        BFGS(nodes, neighbors, check_node)
    except ValueError:
        return False

    return True


