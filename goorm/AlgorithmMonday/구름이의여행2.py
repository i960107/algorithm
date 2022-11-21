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


def solution2(n: int, k: int, graph: Dict[int, List[int]]):
    q = deque()
    visited = [0 for _ in range(n + 1)]

    q.append(k)
    while q:
        curr = q.popleft()

        for next in graph[curr]:
            if visited[next] == 0:
                visited[next] = visited[curr] + 1
                q.append(next)
            if next == k:
                break
    return visited[k] if visited[k] else -1


n, m, k = map(int, input().split())
bridges = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    bridges[a].append(b)
print(solution2(n, k, bridges))
