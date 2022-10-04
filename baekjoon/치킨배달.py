from itertools import combinations
from typing import List


# def solution(N: int, M: int, city: List[List[int]]) -> int:
#     def get_house_position() -> List[Tuple[int, int]]:
#         houses = []
#         for i in range(N):
#             for j in range(N):
#                 if city[i][j] == 1:
#                     houses.append((i, j))
#         return houses
#
#     def brute_force(idx: int, x: int, y: int) -> int:
#         '''치킨집 m개를 선택하기 위한 방법'''
#         if idx == M:
#             choice_chicken = []
#             for i in range(N):
#                 for j in range(N):
#                     if city[i][j] == 2:
#                         choice_chicken.append((i, j))
#             result = get_min_dist(choice_chicken, house)
#             return min()
#         else:
#             for i in range(x, n):
#         return 0
#
#     def get_min_dist():
#         '''모든 집과 칰니집 사이의 최단 거리를 구하기'''
#
#     houses = get_house_position()
#     answer = brute_force(0, 0, 0)
#     return answer

def solution(N: int, M: int, city: List[str]):
    houses = []
    chickens = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == "1":
                houses.append((i, j))
            elif city[i][j] == "2":
                chickens.append((i, j))

    min_chicken_distance = 2 * N * len(houses)
    for combi in combinations(chickens, M):
        chicken_distance = 0
        for hi, hj in houses:
            chicken_distance += min(abs(hi - ci) + abs(hj - cj) for ci, cj in combi)
            # dist = N * 2
            # for ci, cj in combi:
            #     dist = min(dist, abs(hi - ci) + abs(hj - cj))
            # chicken_distance += dist
        min_chicken_distance = min(chicken_distance, min_chicken_distance)
    return min_chicken_distance


# N, M = map(int, input().split())
# city = [list(input().split()) for _ in range(N)]
# N, M = 5, 3
# city = ["00100", "00201", "01200", "00100", "00002"]
N, M = 5, 2
city = ["02010", "10100", "00000", "20011", "22012"]
print(solution(N, M, city))
