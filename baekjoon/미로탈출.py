from typing import List
from collections import deque


def solution(maze: List[List[int]]) -> int:
    x, y = 0, 0
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)

    # 시작 좌표 방문 처리
    q = deque()
    q.append((x, y, 1))

    while q:
        x, y, d = q.popleft()
        maze[y][x] = 0

        if x == len(maze[0]) - 1 and y == len(maze) - 1:
            return d

        for k in range(4):
            nx, ny, nd = x + dx[k], y + dy[k], d + 1
            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] == 1:
                q.append((nx, ny, nd))


res = solution([[1, 0, 1, 0, 1, 0],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]])

print(res, res == 10)
