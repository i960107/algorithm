from typing import List
from sys import stdin


def solution(K: int, N: int, cables: List[int]) -> int:
    left, right = 1, max(cables)
    answer = 0
    # 주의! 나눌때는 0으로 나눠지는 경우 없는지 check
    while left <= right:
        mid = left + (right - left) // 2
        cut = 0
        for cable in cables:
            cut += cable // mid
        if cut >= N:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


read = stdin.readline
K, N = map(int, input().split())

cables = []

for _ in range(K):
    cables.append(int(input()))

print(solution(K, N, cables))
