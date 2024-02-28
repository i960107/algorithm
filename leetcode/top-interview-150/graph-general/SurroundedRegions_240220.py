from typing import List


class Solution2:
    # 재귀 호출 횟수를 줄이려면 어떤 방식으로 dfs하는 것이 좋을까?
    # edge case not handled correctly -> border에서 시작하는 경우?
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dr = (0, 0, 1, -1)
        dc = (1, -1, 0, 0)
        o = "O"
        x = "X"

        visited = [[False] * n for _ in range(m)]

        # 중요한 것 은 방문 체크
        # number of islands는 한번 방문한 곳을 flip함으로써 방문체크가 됨.

        def isInside(r: int, c: int) -> bool:
            res = True
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if not (0 <= nr < m and 0 <= nc < n):
                    res = False
                    continue

                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True

                if board[nr][nc] == x:
                    continue

                # 한번이라도 조건에 반하는 경우 나오면 바로 종료 더 dfs할 필요가 없음.
                # 전체 영역 visited 안하고 일부 영역만 체크후 다음 번에 visitede 된 곳은 continue함으로 incorrect하게 작동함.
                res &= isInside(nr, nc)
            return res

        def flip(r: int, c: int):
            board[r][c] = x
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                # 내부 영역에 대해서만 flip하기 때문에 index out of bound 경우 없음.
                # if not (0 <= nr < m and 0 <= nc < n):
                #     continue
                if board[nr][nc] == x:
                    continue

                flip(nr, nc)

        # visited 두번 체크해주어야하나 isInside, flip?
        # flip은 연결된 곳은 모두 x로 flip하기 때문에 방문체크할 필요 없음
        for r in range(m):
            for c in range(n):
                # visitedc 체크해주어야. 이전에 방문한 영역이어도 내부가 아니어서 flip되지 않았을 수 있음.
                if visited[r][c]:
                    continue
                visited[r][c] = True

                if board[r][c] == x:
                    continue

                result = isInside(r, c)
                print(result, r, c)
                if result:
                    flip(r, c)

        for row in board:
            print(row)


s = Solution2()
# print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
# 맞닿아있는 4면중 범위를 벗어나는 곳이 있는지체크하기 때문에 edge-connected o에서 dfs 시작해도 false 반환됨.
# print(s.solve([
#     ["X", "X", "O", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"]]))
print(s.solve([["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
               ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
               ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
               ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
               ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
               ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
               ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
               ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
               ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
               ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]))


# print(s.solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))

class Solution:
    # 재귀 호출 횟수를 줄이려면 어떤 방식으로 dfs하는 것이 좋을까?
    # edge case not handled correctly -> border에서 시작하는 경우?
    # 왜 성능이 훨씬 더 좋지?
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dr = (0, 0, 1, -1)
        dc = (1, -1, 0, 0)
        flip = "O"
        nothing = "X"
        exclude = "E"

        def mark(r, c):
            board[r][c] = exclude
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if board[nr][nc] != flip:
                    continue
                mark(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == nothing:
                    continue
                if r not in [0, rows - 1] and c not in [0, cols - 1]:
                    continue
                mark(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == exclude:
                    board[r][c] = flip
                elif board[r][c] == flip:
                    board[r][c] = nothing
