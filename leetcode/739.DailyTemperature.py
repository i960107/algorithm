from typing import List


def solution(T: List[int]) -> List[int]:
    stack = []
    answer = [0] * len(T)
    for day, temp in enumerate(T):
        while stack and T[stack[-1]] < temp:
            prev_day = stack.pop()
            answer[prev_day] = day - prev_day
        stack.append(day)

    return answer


print(solution([73, 74, 75,71, 69, 72, 76, 73]))
