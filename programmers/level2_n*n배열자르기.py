from typing import List


def solution(n: int, left: int, right: int) -> List[int]:
    answer = [0] * (right - left)
    for i in range(len(answer)):
        # (i // n) 행 (i % n) -1 열
        answer[i] =
    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
