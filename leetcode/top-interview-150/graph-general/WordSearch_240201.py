from typing import List
from collections import defaultdict, Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 그냥 bfs랑 다른 점은?
        # 바로 방문처리해도 되나?
        # 한번 방문한 곳 다시 방문하지 않도록 매 라운드마다 visited 처리
        # 전체 visited 처리 아님!
        rows, cols = len(board), len(board[0])

        dr = (0, 0, 1, -1)
        dc = (1, -1, 0, 0)

        # 현재 위치 r,c 다음으로 비교해야할 인덱스 i + 1
        # 현재 위치에 대한 비교 끝남. word[i] == board[r][c]인 상태
        def dfs(r: int, c: int, i: int):
            if i == len(word) - 1:
                nonlocal found
                found = True
                return

            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if word[i + 1] != board[nr][nc]:
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                dfs(nr, nc, i + 1)
                visited[nr][nc] = False

        found = False
        visited = [[False] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if found:
                    break
                if word[0] == board[r][c]:
                    visited[r][c] = True
                    dfs(r, c, 0)
                    visited[r][c] = False
        return found

    def exist2(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        boardDict = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                boardDict[board[r][c]] += 1

        wordDict = Counter(word)
        for c in wordDict:
            if c not in boardDict or boardDict[c] < wordDict[c]:
                return False
        def dfs(r:int, c:int, i:int):
            if i < 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True





s = Solution()
print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
