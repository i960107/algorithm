from typing import List


def solution(board: List[List[int]]) -> int:
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    def dfs(x: int, y: int):
        board[y][x] = -1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == 0:
                dfs(nx, ny)

    count = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                dfs(x, y)
                count += 1
    return count


res = (solution([[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]))
print(res, res == 3)
