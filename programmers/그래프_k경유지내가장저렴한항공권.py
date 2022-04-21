from typing import List
from collections import defaultdict
import heapq


def solution(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    # 전체 노드가 아닌 K개의 경유지 내에 도착하는 가격
    # 출발지와 도착지가 정해져있음

    graph = defaultdict(list)
    for a, b, cost in flights:
        graph[a].append((b, cost))

    # 전체 거리를 보관할 필요 없음. 도착점까지의 최단 경로만 구하면 됨
    # dist = defaultdict(int)
    # 큐변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    while Q:
        cost, node, k = heapq.heappop(Q)
        if node == dst:
            return cost
        # K이내일때만 경로를 추가하여, K를 넘어서는 경로는 더 이상 탐색되지 않도록
        if k >= 0:
            for v, w in graph[node]:
                alt = cost + w
                heapq.heappush(Q, (alt, v, k - 1))
        else:
            break
    # 전체 경로의 개수도 체크할 필요 없음
    return -1


print(solution(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
