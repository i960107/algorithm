from typing import List
from collections import deque

'''2차원 격자의 #로 둘러쌓인 면적 구하기'''


# .점으로 bfs를 하면 되나?


def solution(input: List[str]) -> int:
    # grid = [row.split() for row in grid]
    grid = []

    # 행, 열의 길이
    n, m = len(input), len(input[0])
    for r in range(n):
        row = []
        for c in range(m):
            row.append(input[r][c])
        grid.append(row)

    queue = deque()

    # 상, 오른쪽 위, 우, 오른쪽 아래, 하, 왼쪽 아래, 왼쪽, 왼쪽 위 아님 네방향망.
    # dr = (-1, -1, 0, 1, 1, 1, 0, -1)
    # dc = (0, 1, 1, 1, 0, -1, - 1, - 1)
    # 상, 하, 좌, 우
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    for r in range(n):
        for c in range(m):
            if not (r in (0, n - 1) or c in (0, m - 1)):
                continue
            if grid[r][c] == ".":
                queue.append((r, c))

    area = 0
    while queue:
        cr, cc = queue.popleft()
        if grid[cr][cc] != ".":
            continue

        area += 1
        grid[cr][cc] = "~"

        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]

            if not (0 <= nr < n and 0 <= nc < m):
                continue
            queue.append((nr, nc))
            return n * m - area


# print(solution([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]))
# print(solution([".#.", "#..", ".#."]))
print(solution(["####", "##.#", ".#.#"]))
