from sys import stdin
from collections import defaultdict, deque
from typing import Dict, List


def solution(n: int, friends: Dict[int, List[int]]):
    visited = [False] * (1 + n)
    bfs_queue = deque()
    bfs_queue.append((1, 0))
    visited_nodes = []

    while bfs_queue:
        curr, depth = bfs_queue.popleft()
        if visited[curr]:
            continue
        visited[curr] = True
        visited_nodes.append(curr)

        for next in friends[curr]:
            bfs_queue.append((next, depth + 1))
    return len(visited_nodes)


n = int(input())
m = int(input())
read = stdin.readline
friends = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)
print(solution(n, friends))
