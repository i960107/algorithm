from collections import defaultdict
from typing import Dict, List
from sys import stdin, setrecursionlimit


def get_max_water_tank_count_in_cyclic_path(N: int, adj: Dict[int, List[int]]) -> List[int]:
    # 순환하는 수로라면 그 path를 반환 아니라면 []를 반환
    visited = [False for _ in range(1 + N)]
    circle = []
    # 기본값 -2 혹은 직전 방문한 노드의 번호
    found = -1

    def find_cycle(u: int, target: int):
        nonlocal found

        # 방문 기록이 있다면, 순환 구조라고 할 수 있다
        # 순환되는 고리는 단 1이기 때문이다
        if visited[u]:
            found = u
            if u not in circle:
                circle.append(u)
            return

        # 방문 기록이 없다면 방문 기록을 남긴다
        visited[u] = True

        # 도착한 물탱크에서 갈 수 있는 물탱크들로 물ㅇ르 보낸다
        for v in adj[u]:

            # 만약 물을 공급받은 물탱크라면 탐색 정지
            if v == target:
                continue

            find_cycle(v, u)

            # 이미 발견된 순환 고리 값이라면 탐색 정지
            if found == -2:
                return

            # 탐색한 경로에서 u를 방문했다
            # 이미 방문된 지점이기 때문에 탐색 정지
            if found == u:
                found = -2
                return

            # 새롭게 발견한 순환 고리 값이라면 순환 고리에 추가하고, 탐색 종료
            if found >= 0:
                if u not in circle:
                    circle.append(u)
                return

    find_cycle(1, 1)
    return circle


read = stdin.readline
setrecursionlimit(10 ** 8)

N = int(input())
adj = defaultdict(list)
for _ in range(N):
    a, b = map(int, read().split())
    adj[a].append(b)
    adj[b].append(a)

res = (get_max_water_tank_count_in_cyclic_path(N, adj))
print(len(res))
print(*sorted(res))
