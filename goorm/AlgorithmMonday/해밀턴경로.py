from collections import defaultdict

from typing import List, Dict


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
adj = defaultdict(list)
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


# 해밀턴 경로: 모든 정점을 한번씩만 방문할 수 있는 경로.
# 모든 정점을 한번씩 방문한 후 다시 출발 정점으로 돌아올 수 있는 경로 해밀턴 회로
# 어디서 시작하느냐 중요. 단 u -> v 해밀턴 경로가 있다면 v->e해밀턴 경로도 존재
# 각 노드에서 가능한 모든 경로를 살펴야 하나.? 그 중 가장 긴 경로..

def dfs(now: int, path: List[int], visited: List[bool]) -> List[int]:
    path.append(now)
    visited[now] = True

    global answer
    if len(path) > answer:
        answer = len(path)

    for nxt in adj[now]:
        if visited[nxt]:
            continue
        dfs(nxt, path, visited)

    path.pop()
    visited[now] = False


hamilton = False
for v in range(1, V + 1):
    answer = 0
    visited = [False] * (V + 1)
    path = []
    dfs(v, path, visited)
    if answer == V:
        hamilton = True

print("YES" if hamilton else "NO")
