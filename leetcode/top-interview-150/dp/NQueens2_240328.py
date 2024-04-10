from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0

        cols = set()
        negDiag = set()  # r + c
        posDiag = set()  # r - c

        def dfs(r: int):
            nonlocal count
            if r == n:
                count += 1
            for c in range(n):
                if c in cols or r + c in negDiag or r - c in posDiag:
                    continue

                cols.add(c)
                negDiag.add(r + c)
                posDiag.add(r - c)

                dfs(r + 1)

                cols.remove(c)
                negDiag.remove(r + c)
                posDiag.remove(r - c)

        dfs(0)
        return count


s = Solution()
print(s.totalNQueens(4))
print(s.totalNQueens(1))
