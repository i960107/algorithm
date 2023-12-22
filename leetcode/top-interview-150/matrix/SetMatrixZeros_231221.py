from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows = set()
        columns = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows.add(r)
                    columns.add(c)

        for r in range(m):
            for c in range(n):
                if r in rows or c in columns:
                    matrix[r][c] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])

        # rows, prepping cols
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for k in range(col):
                        if matrix[i][k] == 0:
                            matrix[i][k] = None
                        else:
                            matrix[i][k] = 0
                    break

        # 원래 0이었던 것 -> col돌때 전체 row에 대해서 0으로 바꾸어줘야함. 영향받아서 0이 되었던 것은 지나쳐야함.
        # doing cols
        for i in range(col):
            for j in range(row):
                if matrix[j][i] is None:
                    for k in range(row):
                        matrix[k][i] = 0
                    # 전체 row에 대한 처리 끝났으므로 볼 필요 없음.
                    break


s = Solution()
print(s.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
