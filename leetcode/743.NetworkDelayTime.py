from typing import List
from collections import defaultdict
import heapq


def network_delaytime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))
    # Q 원소: (소요시간, 정점) 소요시간이 작을수록 우선순위 높음
    Q = [(0, k)]
    dist = defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for next_node, next_time in graph[node]:
                heapq.heappush(Q, (time + next_time, next_node))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == n:
        return max(dist.values())
    return -1


print(network_delaytime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(network_delaytime([[1, 2, 1]], 2, 1))
print(network_delaytime([[1, 2, 1]], 2, 2))
