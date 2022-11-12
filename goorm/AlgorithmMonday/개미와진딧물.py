from typing import List, Tuple
from collections import deque


def get_ant_houses_not_affected_by_aphid(n: int, m: int, grid: List[List[int]]) -> int:
    aphids = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                aphids.append((i, j))

    move = set()
    for i in range(m + 1):
        for j in range(m + 1 - i):
            move.add((i, j))
            move.add((- i, j))
            move.add((i, -j))
            move.add((-i, -j))
    move = list(move)

    affected = [[False] * n for _ in range(n)]

    while aphids:
        i, j = aphids.pop()
        for k in range(len(move)):
            ni, nj = i + move[k][0], j + move[k][1]
            if 0 <= ni < n and 0 <= nj < n:
                affected[ni][nj] = True

    count = 0
    for i in range(n):
        for j in range(n):
            if affected[i][j] == True and grid[i][j] == 1:
                count += 1
    return count


def get_ant_house_locations(grid: List[List[int]]) -> List[Tuple[int, int]]:
    ants = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                ants.append((i, j))
    return ants


def traverse_aphid_in_distance(i: int, j: int, m: int, grid: List[List[int]]) -> bool:
    di = (0, 0, 1, -1)
    dj = (1, -1, 0, 0)

    def is_aphid(i: int, j: int) -> bool:
        return grid[i][j] == 2

    bfs_queue = deque()
    bfs_queue.append((i, j, 0))
    while bfs_queue:
        i, j, d = bfs_queue.popleft()
        for k in range(4):
            ni, nj, nd = i + di[k], j + dj[k], d + 1
            if ni < 0 or ni >= n or nj < 0 or nj >= n or nd > m:
                continue
            if is_aphid(ni, nj):
                return True
            bfs_queue.append((ni, nj, nd))
    return False


def get_ant_house_in_aphid_area(n: int, m: int, grid: List[List[int]]):
    ants = get_ant_house_locations(grid)

    count = 0
    for i, j in ants:
        if traverse_aphid_in_distance(i, j, m, grid):
            count += 1
    return count


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

print(get_ant_houses_not_affected_by_aphid(n, m, grid))
print(get_ant_house_in_aphid_area(n, m, grid))
