from typing import List


def solution(k: int, m: int, score: List[int]) -> int:
    profit = 0
    # 점수가 큰 것 부터 포장하는게 좋음 -> 작은 애들을 제일 적게.
    score.sort()
    for start in range(len(score) - 1, 0, -m):
        end = start - m + 1
        if end < 0:
            break
        profit += score[end] * m
    return profit


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
