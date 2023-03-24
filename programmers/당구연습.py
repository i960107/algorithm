import decimal
from typing import List
from math import sqrt


def solution(m: int, n: int, startX: int, startY: int, balls: List[List[int]]) -> List[int]:
    answer = []
    # float을 어떻게 처리하느냐. 부동 소수점 문제를 어떻게 해결하느냐..
    for x, y in balls:
        midX = (startX + x) / 2
        midY = (startY + y) / 2
        walls = [(midX, 0), (midX, n), (0, midY), (m, midY)]
        min_distance = int(1e9)
        # x == startX or y == startY인경우
        for wx, wy in walls:
            #  불가능한 경우 언제?
            # start와 벽사이에 공이 있는 경우 불가능
            if y == startY and (wx < x < startX or startX < x < wx):
                continue
            if x == startX and (wy < y < startY or startY < y < wy):
                continue
            distance = 0
            # 대각선으로 원큐선 성공하는 경우는 어떻게 처리하지?
            # start point와의 거리
            distance += ((wx - startX) ** 2 + (wy - startY) ** 2) ** 0.5
            distance += ((wx - x) ** 2 + (wy - y) ** 2) ** 0.5
            distance **= 2
            # 공과의 거리
            print("공", (x, y), "벽", (wx, wy), distance)
            min_distance = min(min_distance, round(distance))
        answer.append(min_distance)
    return answer


# (3,7) -> (7,3)을 칠때 두 공 사이 벽을 맞추는게 가까울까 대각 선을 맞추는게 가까울 까
print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
