from typing import List
from collections import defaultdict
import heapq


def solution(n: int, vertex: List[List[int]]) -> int:
    INF = int(1e9)
    distance = [INF for _ in range(n + 1)]

    adj = defaultdict(list)
    for a, b in vertex:
        adj[a].append(b)
        adj[b].append(a)

    queue = []
    queue.append((0, 1))
    distance[1] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for nxt in adj[now]:
            if distance[nxt] <= dist + 1:
                continue
            distance[nxt] = dist + 1
            heapq.heappush(queue, (dist + 1, nxt))

    max_distance, count = 0, 0
    for node in range(1, n + 1):
        dist = distance[node]
        if dist > max_distance:
            max_distance, count = dist, 1
        elif dist == max_distance:
            count += 1
    return count


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
