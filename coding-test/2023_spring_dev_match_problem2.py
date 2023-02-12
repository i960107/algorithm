from typing import List, Union
from collections import deque

'''2차원 격자의 #로 둘러쌓인 면적 구하기'''


# .점으로 bfs를 하면 되나?


def solution(input: List[str]) -> int:
    # row.split()은 공백을 기준으로 분리하기 때문에 문자열 분리안됨.
    # grid = [row.split() for row in grid]
    grid = [[x for x in row] for row in input]

    # 행, 열의 길이
    n, m = len(input), len(input[0])

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


def solution_in_area(input: List[Union[str, int]]) -> int:
    grid = [[x for x in row] for row in input]
    n, m = len(grid), len(grid[0])
    sequence = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "#":
                sequence += 1
                bfs(sequence, grid, r, c)

    return get_area_width(sequence, grid)


def get_area_width(n: int, grid: List[List[Union[str, int]]]) -> int:
    width = 0
    for r in range(len(grid)):
        area = [None] * (n + 1)
        for c in range(len(grid[r])):
            curr = grid[r][c]
            # 숫자와 문자를 비교하면?
            if curr == ".":
                continue

            if area[curr] is not None:
                pass
        for index in area:
            if index:
                width += 1
    return width


def bfs(sequence: int, grid: List[List[str]], r: int, c: int):
    n, m = len(grid), len(grid[0])

    queue = deque()
    queue.append((r, c))

    dr = (-1, -1, 0, 1, 1, 1, 0, -1)
    dc = (0, 1, 1, 1, 0, -1, - 1, - 1)
    d = len(dr)

    while queue:
        cr, cc = queue.pop()
        if grid[cr][cc] != "#":
            continue
        grid[cr][cc] = sequence
        for k in range(d):
            nr, nc = cr + dr[k], cc + dc[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            queue.append((nr, nc))


# print(solution([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]))
# print(solution([".#.", "#..", ".#."]))
# print(solution(["####", "##.#", ".#.#"]))
# print()
# print(solution_in_area([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]))
# print(solution_in_area([".#.", "#..", ".#."]))
print(solution_in_area(["####", "##.#", ".#.#"]))
