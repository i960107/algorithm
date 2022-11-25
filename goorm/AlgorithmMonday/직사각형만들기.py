from typing import List
from collections import Counter


def solution(n: int, sticks: List[int]) -> int:
    counter = Counter(sticks)
    s = []
    for x, cnt in counter.items():
        s += ([x] * (cnt // 2))
    s.sort(reverse=True)
    area = 0

    for i in range(0, len(s) - 1, 2):
        x = s[i]
        y = s[i + 1]
        area += x * y
    return area


print(solution(8, [2, 4, 6, 8, 2, 4, 6, 8]))
print(solution(4, [4, 8, 4, 8, 4, 8]))
print(solution(6, [1, 1, 3, 3, 2, 4]))
# n = int(input())
# sticks = list(map(int, input().split()))
# print(solution(n, sticks))
