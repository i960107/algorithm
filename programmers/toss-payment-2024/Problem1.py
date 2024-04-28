from typing import List


def solution(levels: List[int]) -> int:
    levels.sort(reverse=True)
    count = int(len(levels) / 4)
    return levels[count - 1] if 0 <= count - 1 < len(levels) else - 1


# 상위 25% 이내의 난이도를 가진 문제 중 가장 쉬운 문제 고르기
# 각 문제의 레벨은 다 다르다.
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
