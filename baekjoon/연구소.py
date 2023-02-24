from typing import List, Final
from itertools import combinations


def solution(N: int, M: int, grid: List[List[int]]) -> int:
    EMPTY: Final = 0
    WALL: Final = 1
    VIRUS: Final = 2

    EXTRA_WALLS: Final = 3


    area = N * M

    empty_places = []
    virus_places = []
    walls = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == EMPTY:
                empty_places.append((r, c))
            elif grid[r][c] == WALL:
                walls += 1
            elif grid[r][c] == VIRUS:
                virus_places.append((r, c))

    max_safe_area = 0

    for combi in combinations(empty_places, EXTRA_WALLS):
        for r, c in combi:
            grid[r][c] = WALL

        count = 0
        visited = [[False] * M for _ in range(N)]

        for r, c in virus_places:
            count += bfs(r, c, grid, visited)

        safe_area = area - (walls + EXTRA_WALLS) - count
        max_safe_area = max(max_safe_area, safe_area)

        for r, c in combi:
            grid[r][c] = EMPTY

    return max_safe_area


def bfs(r: int, c: int, grid: List[List[int]], visited: List[List[bool]]) -> int:
    DR: Final = (0, 0, 1, -1)
    DC: Final = (1, -1, 0, 0)
    pass


N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
print(solution(N, M, grid))
