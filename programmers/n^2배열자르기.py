from typing import List


def solution(n: int, left: int, right: int) -> List[int]:
    answer = [0] * (right - left + 1)
    for index, sequence in enumerate(range(left, right + 1)):
        r, c = sequence // n, sequence % n
        if r >= c:
            answer[index] = (r + 1)
        else:
            answer[index] = (r + 1) + (c - r)
    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
