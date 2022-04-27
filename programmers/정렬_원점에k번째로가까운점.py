import heapq
import math
from typing import List


def k_closest_point(points: List[List[int]], K: int) -> List[List[int]]:
    # O(NlogN)
    points.sort(key=lambda x: (x[0] * x[0] + x[1] * x[1]))
    return points[:K]


def k_closest_point_heapq(points: List[List[int]], K: int) -> List[List[int]]:
    '''유클리드 거리의 우선순위 큐'''
    # K번 추출이라는 단어에서 바로 우선순위 큐를 떠올릴 수 있다.
    # 만약 가장 먼거리를 출력해야 한다면 거리를 음수로 변환하여 삽입

    q = []
    # O(NlogN)
    for x, y in points:
        # math.sqrt 불필요한 계산 줄여서 최적화 가능
        dist = math.sqrt(x * x + y * y)
        heapq.heappush(q, (dist, x, y))

    answer = []
    # O(KlogN)
    for _ in range(K):
        answer.append(list(heapq.heappop(q)[1:]))
    return answer


print(k_closest_point([[1, 3], [-2, 2]], 1))
print(k_closest_point([[3, 3], [5, -1], [-2, 4]], 2))

print(k_closest_point_heapq([[1, 3], [-2, 2]], 1))
print(k_closest_point_heapq([[3, 3], [5, -1], [-2, 4]], 2))
