from graph import build_subway_graph, draw_graph
import networkx as nx
from utils import input_stations
from collections import deque


def dfs_path(graph: nx.Graph, a: str, b: str):
    return get_path(graph, a, b, lambda stack: stack.pop())


def bfs_path(graph: nx.Graph, a: str, b: str):
    return get_path(graph, a, b, lambda queue: queue.popleft())


def get_path(graph: nx.Graph, a: str, b: str, pop_func):
    queue = deque([(a, [a])])
    visited = set()

    while queue:
        current, path = pop_func(queue)
        if current in visited:
            continue
        visited.add(current)

        if current == b:
            return path

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []


def main():
    """
    Stations: ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']
    Enter first station: A1
    Enter second station: A7
    BFS path: ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
    DFS path: ['A1', 'A2', 'A3', 'B2', 'B3', 'B4', 'C2', 'C3', 'C4', 'A6', 'A7']
    ---
    BFS traverse the graph by processing neighbour nodes first (FIFO).
    DFS traverse the graph by processing leaf nodes first (LIFO).
    """
    graph = build_subway_graph()
    a, b = input_stations(graph.nodes)
    bfs = bfs_path(graph, a, b)
    dfs = dfs_path(graph, a, b)
    print(f'BFS path: {bfs}')
    print(f'DFS path: {dfs}')
    draw_graph(graph, label='Subway paths', paths=[bfs, dfs])


if __name__ == "__main__":
    main()
