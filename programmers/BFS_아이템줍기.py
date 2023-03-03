from typing import List
from collections import deque


def solution(rectangle: List[List[int]], characterX: int, characterY: int, itemX: int, itemY: int) -> int:
    n = 10
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    for r1, c1, r2, c2 in rectangle:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                grid[r][c] = 1

    def bfs(r: int, c: int):

        dr = (0, 0, 1, -1, 1, 1, -1, -1)
        dc = (1, -1, 0, 0, 1, -1, 1, -1)

        queue = deque()
        queue.append((r, c))

        while queue:

            cr, cc = queue.popleft()
            grid[cr][cc] = -1

            for k in range(8):
                nr, nc = cr + dr[k], cc + dc[k]

                if not (1 <= nr <= n and 1 <= nc <= n):
                    continue

                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    continue

                if grid[nr][nc] == 0:
                    queue.append((nr, nc))

    print('  ' + str([i for i in range(10)]))
    for i, row in enumerate(grid):
        print(i, row)

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            # 테두리이면서 직사각형인 경우
            if (r in (1, n - 1) or c in (1, n - 1)) and grid[r][c] == 1:
                grid[r][c] = 2

            # 테두리 아니면서 직사각형의 가장 바깥 구하기
            if grid[r][c] == 0:
                bfs(r, c)

    print('  ' + str([i for i in range(10)]))
    for i, row in enumerate(grid):
        print(i, row)


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
# print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
# print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
# print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
