import sys
from typing import List
from collections import defaultdict
import heapq


def solution(n: int, start: int, end: int, roads: List[List[int]], traps: List[int]) -> int:
    T = len(traps)
    trap_indices = dict()
    for index, trap in enumerate(traps):
        trap_indices[trap] = index

    adj = defaultdict(list)
    for u, v, w in roads:
        # is_reverse
        adj[u].append((v, w, False))
        adj[v].append((u, w, True))
    # 활성화되지 않았다 -> A가 트랩이 아니거나, A가 트랩이면서 짝수번 밟았다
    # A-> B로 갈 수 있는 경우(양쪽이 활성화되면 방향 그대로, 한쪽만 활성화되면 방향 반대)
    # A -> B로 가는 길이 있고, A,B가 활성화되지 않았을때
    # A -> B로 가는 길이 있고, A, B가 활성화되었을때
    # B -> A로가는 길이 있고, B가 활성화되었을때
    # B -> A로 가는 길이 있고 A가 활성화되었을때

    # distance,노드,  활성화된 트랩들
    INF = sys.maxsize
    queue = [(0, start, 0)]
    distances = [[INF] * (1 << T) for _ in range(n + 1)]

    while queue:
        now_distance, now, activated = heapq.heappop(queue)

        if distances[now][activated] < now_distance:
            continue

        is_now_activated = False
        if now in trap_indices:
            is_now_activated = ((1 << trap_indices[now]) & activated) > 0

        for nxt, cost, is_reverse in adj[now]:
            # 이미 활성화된 트랩인지
            nxt_activated = activated
            is_nxt_already_activated = False
            if nxt in trap_indices:
                is_nxt_already_activated = ((1 << trap_indices[nxt]) & activated) > 0
                nxt_activated = nxt_activated ^ (1 << trap_indices[nxt])
            nxt_distance = now_distance + cost

            if is_reverse and not (is_now_activated ^ is_nxt_already_activated):
                continue

            elif not is_reverse and (is_now_activated ^ is_nxt_already_activated):
                continue

            if distances[nxt][nxt_activated] <= nxt_distance:
                continue
            distances[nxt][nxt_activated] = nxt_distance
            heapq.heappush(queue, (nxt_distance, nxt, nxt_activated))

    min_distance = INF
    for distance in distances[end]:
        if distance < min_distance:
            min_distance = distance

    return min_distance


# print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
