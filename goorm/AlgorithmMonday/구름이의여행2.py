from typing import List, Dict
from collections import deque, defaultdict


def solution(n: int, k: int, bridges: Dict[int, List[int]]):
    queue = deque()
    visited = set()
    queue.append((k, 0))
    while queue:
        curr, depth = queue.popleft()
        if curr == k and depth != 0:
            return depth

        if curr in visited:
            continue
        visited.add(curr)

        for next in bridges[curr]:
            queue.append((next, depth + 1))
    return - 1


n, m, k = map(int, input().split())
bridges = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    bridges[a].append(b)
print(solution(n, k, bridges))
