from typing import List
from collections import deque


def solution(maps: List[List[int]]) -> int:
    n, m = len(maps), len(maps[0])
    target = (n - 1, m - 1)

    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    WALL = 0
    EMPTY = 1

    queue = deque()
    queue.append((0, 0, 1))
    visited = [[False] * m for _ in range(n)]

    while queue:
        r, c, distance = queue.popleft()

        if maps[r][c] == WALL:
            continue

        if visited[r][c]:
            continue
        visited[r][c] = True

        if (r, c) == target:
            return distance

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if not is_valid_coord(n, m, nr, nc):
                continue
            queue.append((nr, nc, distance + 1))

    return -1


def is_valid_coord(n: int, m: int, r: int, c: int) -> bool:
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
