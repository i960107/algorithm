from typing import List, Dict
from collections import defaultdict, deque


class State:
    def __init__(self, node_index: int, depth: int):
        self.node_index = node_index
        self.depth = depth


def get_shortest_path_length(origin: int, dest: int, adj: Dict[int, List[int]]) -> int:
    visited = [False] * (len(adj) + 1)
    # distance[i] := origin에서 i로 가는 최단 경로의 간선의 수
    distance = [-1] * (n + 1)
    queue = deque()
    queue.append(State(origin, 1))

    while queue:
        current = queue.popleft()

        if visited[current.node_index]:
            continue

        visited[current.node_index] = True
        distance[current.node_index] = current.depth - 1

        for next in adj[current.node_index]:
            if visited[next]:
                continue
            queue.append(State(next, current.depth + 1))

    return distance[dest]


n, m = map(int, input().split())
adj = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

origin, dest = map(int, input().split())
answer = get_shortest_path_length(origin, dest, adj)

print(answer)
