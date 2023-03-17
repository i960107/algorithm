import sys
from typing import List, Final, Deque
from collections import deque


class Graph:
    DISCONNECTED: Final = 0

    def __init__(self, V: int):
        self.adj = [[0] * (V + 1) for _ in range(V + 1)]
        self.V = V

    def add_edge(self, src: int, to: int, weight: int):
        self.adj[src][to] = weight

    def has_edge(self, src: int, to: int) -> bool:
        return self.adj[src][to] != self.DISCONNECTED

    def get_distance(self, src: int, to: int) -> int:
        if self.has_edge(src, to):
            return self.adj[src][to]
        else:
            return sys.maxsize


def get_shortest_hamilton_circuit(graph: Graph) -> int:
    origin = 1
    path = deque()
    path.append(origin)
    return __get_shortest_hamilton_circuit__(origin, 1, 0, path, graph)


def __get_shortest_hamilton_circuit__(current_node: int, depth: int, total_length: int, path: Deque,
                                      graph: Graph) -> int:
    if depth == graph.V:
        origin = path[0]

        if graph.has_edge(current_node, origin):
            return total_length + graph.get_distance(current_node, origin)
        else:
            return sys.maxsize

    min_length = sys.maxsize
    # 이미 끝까지 탐색한 해밀턴 경로 중 더 짧은 경로가 있다면 탐색할 필요 없음
    for next_node in range(1, graph.V + 1):
        if not graph.has_edge(current_node, next_node) or next_node in path:
            continue

        next_length = total_length + graph.get_distance(current_node, next_node)
        if next_length >= min_length:
            continue

        path.append(next_node)

        length = __get_shortest_hamilton_circuit__(next_node, depth + 1, next_length, path, graph)
        min_length = min(min_length, length)

        path.pop()

    return min_length


N = int(input())
graph = Graph(N)
for src in range(1, N + 1):
    for to, weight in enumerate(map(int, input().split()), 1):
        graph.add_edge(src, to, weight)

answer = get_shortest_hamilton_circuit(graph)
if answer == sys.maxsize:
    print("NO PATH")
else:
    print(answer)
