import sys
from typing import List
from collections import defaultdict
import heapq

INF = sys.maxsize


# def solution_fail(n: int, start: int, end: int, roads: List[List[int]], traps: List[int]) -> int:
#     answer = INF
#     adj = defaultdict(list)
#     # 각 함정노드의 활성화여부...
#     # 현재 노드의 활성화여부만 체크하면 안됨. 지나온 경로에서의 활성화여부 체크해야함. -> 비트마스크 활용
#     #  0 ~ 에서 2 ** len(traps)개의 수가 필요
#     # 다익스트라 필요없이 bfs로 최단거리 찾으면됨.
#     visited = [[False for _ in range(2 ** len(traps) + 1)] for _ in range(n + 1)]
#
#     temp = defaultdict(lambda: (False, 0))
#     for i, t in enumerate(traps):
#         temp[t] = (True, i)
#     # 노드번호: trap인지, 인덱스를 기록.
#     traps = temp
#
#     for u, v, w in roads:
#         # True : 정방향, False:역방향
#         adj[u].append((v, w, True))
#         adj[v].append((u, w, False))
#
#     # 2진수 0을 말함.
#     active = 0b0
#     queue = [(0, start, active)]
#
#     while queue:
#         weight, now, active = heapq.heappop(queue)
#
#         # 가중치가 낮은게 먼저 꺼내지긴 하지만, active에 따라서 여러 경우가 있기 때문에
#         # 가장 먼저 꺼내졌다고 항상 최단거리는 아님
#         if visited[now][active]:
#             continue
#
#         visited[now][active] = True
#         now_is_trap = False
#         # 현재 트랩 활성화 추가.
#         if traps[now][0]:
#             now_is_trap = True
#             active = active ^ (1 << traps[now][1])
#
#         if now == end:
#             answer = min(answer, weight)
#
#         # active에서 각 노드가 활성화되었는지 어떻게 알 수 있지?


def solution(n: int, start: int, end: int, roads: List[List[int]], traps: List[int]) -> int:
    # 한 미로를 몇번이나 밟을 수 있을까. 미로 밟는 횟수 X  활성화된 미로의 수!
    traps = set(traps)
    temp = dict()
    for i, node in enumerate(traps):
        temp[node] = i
    # 트랩 인덱스 저장
    traps = temp
    T = len(traps)
    adj = defaultdict(list)
    # 정방향, 역방향 둘다 저장해주어야함.
    for u, v, w in roads:
        # is_normal_way? 즉, 정방향 True, 역방향 False
        adj[u].append((v, w, True))
        adj[v].append((u, w, False))

    INF = float('INF')
    # 너무 메모리 많이 차지하므로 visited로 관리해주어도 됨.
    distance = [[INF] * (1 << T) for _ in range(n + 1)]
    queue = []

    queue.append((0, start, 0))
    distance[start][0] = 0

    while queue:
        now_dist, now, activated = heapq.heappop(queue)
        # 가면서 가는 곳이 trap이면 다시 돌아온다...? 그건 아닌데

        if distance[now][activated] < now_dist:
            continue

        is_now_activated = False
        if now in traps:
            is_now_activated = activated ^ (1 << traps[now])
        for nxt, cost, is_normal in adj[now]:
            # actiaved되었으면서 reversed이거나, not actiaved and normal
            nxt_activated = activated
            if nxt in traps:
                nxt_activated = (1 << traps[nxt]) ^ activated
            nxt_dist = now_dist + cost
            if (is_now_activated and is_normal) or (not is_now_activated and not is_normal):
                continue
            if is_now_activated and not is_normal and distance[nxt][nxt_activated] > nxt_dist:
                heapq.heappush(queue, (nxt_dist, nxt, nxt_activated))
            if not is_now_activated and is_normal and distance[nxt][nxt_activated] > nxt_dist:
                heapq.heappush(queue, (nxt_dist, nxt, nxt_activated))
            distance[nxt][nxt_activated] = nxt_dist
    answer = INF
    for activated in range(1 << T):
        dist = distance[end][activated]
        if dist < answer:
            answer = dist
    return answer


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
