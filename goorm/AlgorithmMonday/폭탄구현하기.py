from typing import List, Tuple
from sys import stdin


# def get_affected_area_size(n: int, k: int, bomb: List[Tuple[int]]) -> int:
#     area = [[0] * n for _ in range(n)]
#     dr = (0, 0, 1, -1)
#     dc = (1, -1, 0, 0)
#
#     for row, col in bomb:
#         area[row][col] += 1
#         for k in range(4):
#             new_row = row + dr[k]
#             new_col = col + dc[k]
#             if 0 <= new_row < n and 0 <= new_col < n:
#                 area[new_row][new_col] += 1
#
#     return sum(square for row in area for square in row)
#
#
# n, k = map(int, input().split())
# bomb = []
#
# for _ in range(k):
#     row, col = map(lambda x: int(x) - 1, input().split())
#     bomb.append((row, col))
#
# print(get_affected_area_size(n, k, bomb))

def get_affected_area(n: int, x: int, y: int) -> int:
    '''매번 상,하,좌,우 인덱스 검사'''
    dx = (0, 0, 0, -1, 1)
    dy = (0, 1, -1, 0, 0)

    affected_area = 0
    for dk in range(5):
        nx, ny = x + dx[dk], y + dy[dk]
        if 1 <= nx <= n and 1 <= ny <= n:
            affected_area += 1
    return affected_area


def get_affected_area2(n: int, x: int, y: int) -> int:
    '''위치별로 영향주는 영역의 크기가 달라짐'''
    if 1 < x < n and 1 < y < n:
        return 5
    if x not in (1, n) or y not in (1, n):
        return 4
    return 3


bombs = 0
read = stdin.readline

n, k = map(int, input().split())
for _ in range(k):
    x, y = map(int, input().split())
    bombs += get_affected_area2(n, x, y)
print(bombs)
