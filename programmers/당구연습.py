from typing import List
from math import sqrt


def solution(m: int, n: int, startX: int, startY: int, balls: List[List[int]]) -> List[int]:
    answer = []
    for x, y in balls:
        midX = (startX + x) / 2
        midY = (startY + y) / 2
        walls = [(midX, 0), (midX, n), (0, midY), (m, midY)]
        min_distance = int(1e9)
        # x == startX or y == startY인경우
        for wx, wy in walls:
            distance = int(4 * ((wx - x) ** 2 + (wy - y) ** 2))
            min_distance = min(min_distance, distance)
        answer.append(min_distance)
    return answer


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
