from typing import List
from collections import deque


class Graph:
    def __init__(self, V: int):
        self.adj = [[False] * (V + 1) for _ in range(V + 1)]
        self.V = V
        self.degree = [0] * (V + 1)

    def add_edge(self, u: int, v: int):
        self.adj[u][v] = True
        self.adj[v][u] = True
        self.degree[u] += 1
        self.degree[v] += 1

    def has_edge(self, u: int, v: int) -> bool:
        return self.adj[u][v]

    def get_degree(self, node_index: int) -> int:
        return self.degree[node_index]


def is_connected_graph(graph: Graph) -> bool:
    reachable_nodes = deque()

    visited = [False] * (graph.V + 1)

    original_node = 1
    visit_count = 0
    reachable_nodes.append(original_node)

    while reachable_nodes:
        current_node = reachable_nodes.popleft()

        if visited[current_node]:
            continue

        visited[current_node] = True
        visit_count += 1

        for next_node in range(1, graph.V + 1):
            if graph.has_edge(current_node, next_node):
                reachable_nodes.append(next_node)
    return visit_count == graph.V


def has_euler_path(graph: Graph) -> bool:
    if not is_connected_graph(graph):
        return False

    odd_degree = 0
    for node in range(1, graph.V + 1):
        degree = graph.get_degree(node)
        if degree % 2 == 1:
            odd_degree += 1
    return odd_degree == 0 or odd_degree == 2


def has_euler_circuit(graph: Graph) -> bool:
    if not is_connected_graph(graph):
        return False

    odd_degree = 0
    for node in range(1, graph.V + 1):
        degree = graph.get_degree(node)
        if degree % 2 == 1:
            odd_degree += 1
            break
    return odd_degree == 0


N = int(input())
graph = Graph(N)
for u in range(1, N + 1):
    for v, has_edge in enumerate(map(int, input().split()), 1):
        if has_edge:
            graph.add_edge(u, v)

if has_euler_path(graph):
    print("YES")
else:
    print("NO")

if has_euler_circuit(graph):
    print("YES")
else:
    print("NO")
