import collections
from typing import List
from collections import defaultdict
import heapq


def solution(times: List[List[int]], N: int, K: int) -> int:
    # 모든 노드가 신호를 받는데 걸리는 시간(가장 오래 걸리는 노드까지의 최단 시간) -> 다익스트라 알고리즘으로 추출 가능
    # 모든 노드에 도달할 수 있는지 여부 -> 다익스트라 알고리즘 계산 값이 존재하는지 유무로 판별

    # 딕셔너리로 구현하는 인접 리스트
    graph = defaultdict(list)

    for u, v, w in times:
        # 연결된 노드,도착점을 튜플로 구성
        graph[u].append((v, w))

    # [(소요시간, 정점)] dist의 초깃값을 무한대로 설정하는게 아니라 0으로 설정. heapq모듈의 기능상 제약
    Q = [(0, K)]

    dist = collections.defaultdict(int)
    # heapq모듈은 우선순위 업데이트를 지원하지 않는다(탐색O(N)-자료구조에서 비효율적인 연산)
    # decrease_priority()연산이 필요 없도록
    while Q:
        time, node = heapq.heappop(Q)
        # 큐의 우선순위를 업데이트할 필요 없이 존재 유무로만 진행할 수 있으며 dist에는 항상 최솟값이 셋팅될 것
        # 이미 값이 존재한다면 그값은 이미 최단 경로
        # 인접리스트 고려할 필요 없음
        if node not in dist:
            dist[node] = time
            # 이웃노드를 순회하는것으 ㄴ나중에, dist에 node의 포함여부부터 체크하기.
            for v, w in graph[node]:
                alt = time + w
                # heap q에 원소에 time이 먼저 들어가는 이유. 가중치 계산시 time 사용
                heapq.heappush(Q, (alt, v))

    # 노드에 도달할 수 있는지 여부를 판별
    # 모든 노드의 최단 경로를 구했다는 의미
    if len(dist) == N:
        return max(dist.values())
    return -1
