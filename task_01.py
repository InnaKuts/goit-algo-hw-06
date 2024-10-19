from graph import build_subway_graph, draw_graph
import networkx as nx


def main():
    graph = build_subway_graph()
    draw_graph(graph)

    num_stations = graph.number_of_nodes()
    num_connections = graph.number_of_edges()
    degree_centrality = nx.degree_centrality(graph)

    print(f"Stations: {num_stations}")
    print(f"Connections: {num_connections}")
    print(f"Degree centrality: {degree_centrality}")


if __name__ == "__main__":
    main()
