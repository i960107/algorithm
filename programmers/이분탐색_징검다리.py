from typing import List
from itertools import combinations
from functools import reduce
import operator as op


def solution(distance: int, rocks: list, n: int) -> int:
    # distance 제한 조건이 1,000,000,000으로 매우 크기때문에 이분탐색 필요하다는것 알 수 있음
    # 이분 탐색을 하려면 정렬되어있어야하고, 시작-끝 범위가 분명해야 한다.
    # 바위들 사이 간격은 최대 distance-1
    # left-mid 구간을 선택할지 mid-right구간을 선택할지 고르는 기준은?
    answer = 0
    # 각 바위 사이 거리의 최솟값
    left = 0
    # 각 바위 사이 거리의 최댓값
    right = distance

    # O(N)
    rocks.sort()
    distances = []
    for i in range(len(rocks)):
        distances.append(rocks[i] - rocks[i - 1] if i != 0 else rocks[i])
    print(distances)

    while left < right:
        pass
    return answer


def solution_others(distance: int, rocks: list, n: int) -> int:
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        min_distance = float('inf')
        curr = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - curr
            if diff < mid:
                remove_cnt += 1
            else:
                curr = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer


def solution_practice(distance: int, rocks: List[int], n: int) -> int:
    rocks.sort()
    left, right = 0, distance
    rocks.append(distance)
    answer = 0
    while left <= right:
        # 돌사이의 거리으 최소값
        mid = left + (right - left) // 2
        prev = 0
        removed = 0
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else:
                prev = rock
            if removed > n:
                break
        if removed <= n:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer


print(solution_practice(25, [2, 15, 11, 21, 17], 2))

# print(solution_practice(25, [2, 14, 11, 21, 17, 2], 2))
# def nCr(n: int, r: int) -> int:
#     if n < 1 or r > n or r < 0:
#         raise ValueError
#     r = min(r, n - r)
#     if dp[r] != -1:
#         return dp[r]
#     elif dp[r - 1] != -1:
#         return dp[r - 1] // r * (n - r + 1)
#
#     numerator = reduce(op.mul, range(n, n - r, -1), 1)
#     denominator = reduce(op.mul, range(1, r + 1), 1)
#     return numerator // denominator
#
#
# dp = [-1] * 500001
# max_combi_len = 0
# for r in range(1, 50001):
#     res = nCr(50000, r)
#     max_combi_len = max(max_combi_len, res)
#     dp[r] = res
#
# print(max_combi_len)
