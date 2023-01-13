from collections import defaultdict
from typing import List
import heapq


def cheapest_flights(n: int,flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = defaultdict(list)

    for u, v, p in flights:
        graph[u].append((v, p))

    Q = [(0, src, -1)]
    best_visited = [2 ** 31] * n

    while Q:
        price, node, steps = heapq.heappop(Q)

        if best_visited[node] <= steps or steps > K:
            continue

        # 경유지 개수 비교하는 것과, 도착지인지 확인하는 순서에 따라 정답이 달라짐?
        if node == dst:
            return price

        best_visited[node] = steps

        for v, p in graph[node]:
            heapq.heappush(Q, (price + p, v, steps + 1))

    return -1


print(cheapest_flights(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
print(cheapest_flights(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 2, 2, 0))
print(cheapest_flights(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1))
print(cheapest_flights(6, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2))
