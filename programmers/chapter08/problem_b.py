from typing import List, Dict
from collections import defaultdict, deque

'''인접 리스트를 사용해 구현한 dfs, bfs'''


class State:
    def __init__(self, node_index: int, depth: int):
        self.node_index = node_index
        self.depth = depth


def get_dfs_order(n: int, adj: Dict[int, List[int]]) -> List[int]:
    visited_nodes = []

    dfs_stack = [State(1, 1)]

    visited = [False] * (n + 1)

    while dfs_stack:

        current = dfs_stack.pop()

        if visited[current.node_index]:
            continue
        visited[current.node_index] = True
        visited_nodes.append(current.node_index)

        for ni in range(len(adj[current.node_index]) - 1, -1, -1):
            next = adj.get(current.node_index)[ni]

            if visited[next]:
                continue

            dfs_stack.append(State(next, current.depth + 1))

    return visited_nodes


def get_bfs_order(n: int, adj: Dict[int, List[int]]) -> List[int]:
    visited_nodes = []

    bfs_queue = deque()
    bfs_queue.append(State(1, 1))

    visited = [False] * (n + 1)

    while bfs_queue:
        current = bfs_queue.popleft()

        if visited[current.node_index]:
            continue
        visited[current.node_index] = True
        visited_nodes.append(current.node_index)

        for ni in range(0, len(adj[current.node_index]), 1):
            next = adj.get(current.node_index)[ni]

            if visited[next]:
                continue

            bfs_queue.append(State(next, current.depth + 1))

    return visited_nodes


n, m = map(int, input().split())

adj = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    adj[i] = sorted(set(adj[i]))

dfs_order = get_dfs_order(n, adj)
print('-'.join([str(x) for x in dfs_order]))

bfs_order = get_bfs_order(n, adj)
print('-'.join([str(x) for x in bfs_order]))
