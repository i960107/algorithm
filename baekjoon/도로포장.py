from collections import defaultdict
from typing import List, Dict
import heapq


def solution(N: int, M: int, K: int, adj: Dict[int, List[int]]) -> int:
    # k개 이하의 도로를 포장.
    # 모든 경로를 살펴야함..?
    # 최단 거리인데 경우에 따라 달라짐. I개의 도로를 포장했을때의 최단 거리
    INF = float("INF")
    distance = [[INF for _ in range(K + 1)] for _ in range(N + 1)]
    queue = []
    # distance, city, paved
    queue.append((0, 1, 0))
    for paved in range(K + 1):
        distance[1][paved] = 0

    while queue:
        now_distance, now, paved = heapq.heappop(queue)
        if distance[now][paved] < now_distance:
            continue
        for nxt, cost in adj[now]:

            if distance[nxt][paved] > now_distance + cost:
                distance[nxt][paved] = now_distance + cost
                heapq.heappush(queue, (now_distance + cost, nxt, paved))

            if paved < K and distance[nxt][paved + 1] > now_distance:
                distance[nxt][paved + 1] = now_distance
                heapq.heappush(queue, (now_distance, nxt, paved + 1))

    answer = INF
    for paved in range(K + 1):
        if distance[N][paved] < answer:
            answer = distance[N][paved]
    return answer


N, M, K = map(int, input().split())

adj = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
print(solution(N, M, K, adj))
