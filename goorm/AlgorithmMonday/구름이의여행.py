import sys
from collections import defaultdict, deque
from typing import Dict, List
from sys import setrecursionlimit


class State:
    def __init__(self, node: int, depth: int):
        self.node = node
        self.depth = depth


def can_reach_destination_in_k_bridge_recursive(K: int, N: int, adj: Dict[int, List[int]]) -> bool:
    '''재귀버전-어디가 잘못된건지 모르겠음..'''
    visited = [False] * (N + 1)

    def _dfs(current: State) -> bool:
        if visited[current.node]:
            return False

        elif current.node == N and current.depth <= K + 1:
            return True

        elif current.depth > K + 1:
            return False

        visited[current.node] = True
        for next in adj[current.node]:
            if visited[next]:
                continue
            if _dfs(State(next, current.depth + 1)):
                return True
        visited[current.node] = False
        return False

    return _dfs(State(1, 1))


def can_reach_destination_in_k_bridge_bfs(K: int, N: int, adj: Dict[int, List[int]]) -> bool:
    '''정답 코드'''

    bfs_queue = deque()
    bfs_queue.append((State(1, 1)))
    visited = [False] * (N + 1)
    distance = [K + 1] * (N + 1)

    while bfs_queue:
        current = bfs_queue.popleft()

        if visited[current.node]:
            continue

        elif current.node == N:
            distance[current.node] = current.depth - 1
            break

        elif current.depth > K + 1:
            break

        visited[current.node] = True
        distance[current.node] = current.depth - 1

        for next in adj[current.node]:
            bfs_queue.append(State(next, current.depth + 1))

    return distance[N] <= K


def can_reach_destination_in_k_bridge_stack(K: int, N: int, adj: Dict[int, List[int]]) -> bool:
    '''stack 버전 - timeout 실패'''
    dfs_stack = []

    dfs_stack.append((State(1, 1), [False] * (N + 1)))

    answer = False

    while dfs_stack:
        current, visited = dfs_stack.pop()

        if current.node == N and current.depth <= K + 1:
            answer = True
            break

        elif current.depth > K + 1:
            continue

        elif visited[current.node]:
            continue

        visited[current.node] = True

        for next in adj[current.node]:
            new_visited = visited[:]
            dfs_stack.append((State(next, current.depth + 1), new_visited))

    return answer


N, M, K = map(int, input().split())
adj = defaultdict(list)

sys.setrecursionlimit(10 ** 8)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# print("YES" if can_reach_destination_in_k_bridge_stack(K, N, adj) else "NO")
print("YES" if can_reach_destination_in_k_bridge_recursive(K, N, adj) else "NO")
