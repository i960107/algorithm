from typing import List
from itertools import combinations


def solution(number: List[int]) -> int:
    count = 0
    # combinations, permutations 헷갈리지 말기!
    # combinations 수가 더 작음
    for index1, index2, index3 in combinations(range(len(number)), 3):
        if number[index1] + number[index2] + number[index3] == 0:
            count += 1
    return count


print(solution([-2, 3, 0, 2, -5]))
