from graph import build_subway_graph, draw_graph
import networkx as nx
from utils import input_stations


def main():
    # weight: A1-B5 = 15
    graph = build_subway_graph(weight=lambda s1, s2: int(s1[1:]+s2[1:]))
    a, b = input_stations(graph.nodes)
    path = nx.shortest_path(graph, source=a, target=b, weight='weight', method='dijkstra')
    draw_graph(graph, paths=[path])


if __name__ == "__main__":
    main()
