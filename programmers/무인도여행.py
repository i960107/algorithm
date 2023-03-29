from typing import List
from collections import deque


def solution(maps: List[str]) -> List[int]:
    n, m = len(maps), len(maps[0])
    board = [[int(maps[r][c]) if maps[r][c] != "X" else maps[r][c] for c in range(m)] for r in range(n)]
    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    def bfs(r: int, c: int) -> int:
        queue = deque(())
        queue.append((r, c))
        food = 0
        while queue:
            cr, cc = queue.popleft()
            if board[cr][cc] == "X":
                continue
            food += board[cr][cc]
            board[cr][cc] = "X"
            for k in range(4):
                nr, nc = cr + dr[k], cc + dc[k]
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                queue.append((nr, nc))
        return food

    answer = []
    for r in range(n):
        for c in range(m):
            if board[r][c] != "X":
                result = bfs(r, c)
                answer.append(result)
    if not answer:
        return [-1]

    answer.sort()

    return answer


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))
