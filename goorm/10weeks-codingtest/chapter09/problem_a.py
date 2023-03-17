from typing import List


class Graph:
    def __init__(self, V: int):
        self.adj = [[False] * (V + 1) for _ in range(V + 1)]
        self.V = V

    def add_edge(self, u: int, v: int):
        self.adj[u][v] = True
        self.adj[v][u] = True

    def has_edge(self, u: int, v: int) -> bool:
        return self.adj[u][v]


def __has_hamilton_path__(depth: int, current_node: int, visited: List[bool], graph: Graph) -> bool:
    if visited[current_node]:
        return False

    visited[current_node] = True

    has_path = False

    if depth == graph.V:
        has_path = True

    else:
        for nxt_node in range(1, graph.V + 1):
            has_path = __has_hamilton_path__(depth + 1, nxt_node, visited, graph)
            if has_path:
                break

    visited[current_node] = False
    return has_path


def has_hamilton_path(graph: Graph) -> bool:
    visited = [False] * (graph.V)
    for original_node in range(1, graph.V + 1):
        has = __has_hamilton_path__(1, original_node, visited, graph)
        if has:
            return True
    return False


V, E = map(int, input().split())
graph = Graph(V)

for _ in range(E):
    u, v = map(int, input().split())
    graph.add_edge(u, v)

has_path = has_hamilton_path(graph)
if has_path:
    print("YES")
else:
    print("NO")
