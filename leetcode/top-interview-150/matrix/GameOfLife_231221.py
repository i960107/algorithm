from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        LIVE, DEAD = 1, 0
        REPRODUCED, DIES = 2, 3
        dr = (-1, -1, 0, 1, 1, 1, 0, -1)
        dc = (0, 1, 1, 1, 0, -1, -1, -1)
        k = 8
        for r in range(m):
            for c in range(n):
                count = 0
                for i in range(k):
                    nr, nc = r + dr[i], c + dc[i]
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if board[nr][nc] == LIVE or board[nr][nc] == DIES:
                        count += 1
                print("rc", r, c, count)
                if board[r][c] == DEAD:
                    if count == 3:
                        board[r][c] = REPRODUCED
                else:
                    if 2 <= count <= 3:
                        continue
                    board[r][c] = DIES

        for r in range(m):
            for c in range(n):
                if board[r][c] == REPRODUCED:
                    board[r][c] = LIVE
                elif board[r][c] == DIES:
                    board[r][c] = DEAD
        return board


s = Solution()
print(s.gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
