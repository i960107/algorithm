from sys import stdin
from collections import defaultdict, deque
from typing import Dict, List


def solution_bfs(n: int, friends: Dict[int, List[int]]):
    visited = [False] * (1 + n)
    bfs_queue = deque()
    bfs_queue.append(1)

    answer = 0
    while bfs_queue:
        curr = bfs_queue.popleft()

        if visited[curr]:
            continue
        visited[curr] = True
        answer += 1

        for next in friends[curr]:
            bfs_queue.append(next)

    return answer


def solution_dfs(n: int, friends: Dict[int, List[int]]):
    res = 0
    visited = [False] * (n + 1)

    def _dfs(node: int):
        if visited[node]:
            return
        visited[node] = True
        nonlocal res
        res += 1
        for next in friends[node]:
            _dfs(next)

    _dfs(1)
    return res


n = int(input())
m = int(input())
read = stdin.readline
friends = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)
print(solution_bfs(n, friends))
print(solution_dfs(n, friends))
