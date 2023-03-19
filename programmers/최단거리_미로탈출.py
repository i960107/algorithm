import sys
from typing import List
from collections import defaultdict
import heapq

INF = sys.maxsize


def solution(n: int, start: int, end: int, roads: List[List[int]], traps: List[int]) -> int:
    answer = INF
    adj = defaultdict(list)
    # 각 함정노드의 활성화여부...
    # 현재 노드의 활성화여부만 체크하면 안됨. 지나온 경로에서의 활성화여부 체크해야함. -> 비트마스크 활용
    #  0 ~ 에서 2 ** len(traps)개의 수가 필요
    # 다익스트라 필요없이 bfs로 최단거리 찾으면됨.
    visited = [[False for _ in range(2 ** len(traps) + 1)] for _ in range(n + 1)]

    temp = defaultdict(lambda: (False, 0))
    for i, t in enumerate(traps):
        temp[t] = (True, i)
    # 노드번호: trap인지, 인덱스를 기록.
    traps = temp

    for u, v, w in roads:
        # True : 정방향, False:역방향
        adj[u].append((v, w, True))
        adj[v].append((u, w, False))

    # 2진수 0을 말함.
    active = 0b0
    queue = [(0, start, active)]

    while queue:
        weight, now, active = heapq.heappop(queue)

        # 가중치가 낮은게 먼저 꺼내지긴 하지만, active에 따라서 여러 경우가 있기 때문에
        # 가장 먼저 꺼내졌다고 항상 최단거리는 아님
        if visited[now][active]:
            continue

        visited[now][active] = True
        now_is_trap = False
        # 현재 트랩 활성화 추가.
        if traps[now][0]:
            now_is_trap = True
            active = active ^ (1 << traps[now][1])

        if now == end:
            answer = min(answer, weight)

        # active에서 각 노드가 활성화되었는지 어떻게 알 수 있지?
        for nxt in adj[]


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))

print(int(0b0))
print(0b0)
