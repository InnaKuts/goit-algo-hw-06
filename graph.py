from typing import Callable
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes import graph
from utils import pairwise


def build_subway_graph(weight: Callable[[str, str], int] = None) -> graph:
    g = nx.Graph()

    line_1 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
    line_2 = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
    line_3 = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

    g.add_nodes_from(line_1)
    g.add_nodes_from(line_2)
    g.add_nodes_from(line_3)
    edges = (
        list(pairwise(line_1)) +
        list(pairwise(line_2)) +
        list(pairwise(line_3)) +
        [('A6', 'C4'), ('B4', 'C2'), ('A3', 'B2')]
    )

    if weight is None:
        g.add_edges_from(edges)
    else:
        g.add_weighted_edges_from([(e[0], e[1], weight(e[0], e[1])) for e in edges])

    return g


def draw_graph(g: graph, label: str = "Subway", paths: list[list[str]] = None):
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(g)
    nx.draw(
        G=g,
        pos=pos,
        with_labels=True,
        node_size=500,
        node_color='lightblue',
        font_size=10,
        font_weight='bold',
        edge_color='gray',
    )
    if paths is not None:
        for (idx, path) in enumerate(paths):
            color = ((idx % 3)/3, ((idx+1) % 3)/3, ((idx+2) % 3)/3, 0.5)
            nx.draw_networkx_nodes(g, pos, nodelist=[path[0], path[-1]], node_size=550, node_color=[color])
            nx.draw_networkx_edges(g, pos, edgelist=list(pairwise(path)), edge_color=color, width=(idx % 3)+3)
    edge_labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels)

    plt.title(label, size=15)
    plt.show()
