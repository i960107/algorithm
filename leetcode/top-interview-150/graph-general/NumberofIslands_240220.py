from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dr = (0, 0, 1, -1)
        dc = (1, -1, 0, 0)

        LAND = '1'
        WATER = '0'

        def visitLand(r: int, c: int):
            grid[r][c] = WATER

            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] == WATER:
                    continue
                visitLand(nr, nc)

        num = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == WATER:
                    continue
                visitLand(r, c)
                num += 1
        return num


s = Solution()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
