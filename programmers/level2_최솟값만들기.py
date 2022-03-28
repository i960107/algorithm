from typing import List


def solution_get_min_sum(A: List[int], B: List[int]) -> int:
    answer = 0
    for a, b in zip(sorted(A), sorted(B, reverse=True)):
        answer += a * b
    return answer


print(solution_get_min_sum([1, 4, 2], [5, 4, 4]))
print(solution_get_min_sum([1, 2], [3, 4]))
print(solution_get_min_sum([], []))
