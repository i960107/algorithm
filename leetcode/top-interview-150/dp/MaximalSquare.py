from typing import List


class Solution:
    # rectangle 사각형, square 정사각
    # bfs로 섬의 영역찾기도 가능 근데 어떻게 정사각형인 걸 판별할 건데?
    # memoization
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        cache = dict()  # map each (r,c) -> maxLength of square

        # dict의 key가 tuple이 될 수 있는가? O
        # immutable하면 대부분 키가 될 수 있음. list는 안되지만 tuple은 됨.
        max_len = 0

        # matrix[i][j]가 top-left일때 최대 square area
        def dp(r: int, c: int) -> int:
            if r >= rows or c >= cols:
                return 0

            nonlocal max_len

            if (r, c) not in cache:
                down = dp(r + 1, c)
                right = dp(r, c + 1)
                diag = dp(r + 1, c + 1)
                cache[(r, c)] = 0
                # 왜 min값이 되지.
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            if cache[(r, c)] > max_len:
                max_len = cache[(r, c)]
            return cache[(r, c)]

        dp(0, 0)
        return max_len ** 2

    def maximalSquare_memoization(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = int(matrix[r][c])

        @cache
        def dp(r: int, c: int):
            if r >= rows or c >= cols:
                return 0
            if matrix[r][c] == 0:
                return 0
            return min(dp(r + 1, c), dp(r, c + 1), dp(r + 1, c + 1)) + 1

        max_len = 0
        for r in range(rows):
            for c in range(cols):
                result = dp(r, c)
                if result > max_len:
                    max_len = result
        return max_len ** 2

    # tabulation
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_len = 0
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = int(matrix[r][c])

        # Row 0에 1이 있는 경우 체크 안됨.
        # for r in range(1, rows):
        #     for c in range(1, cols):
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    continue
                if r != 0 and c != 0:
                    matrix[r][c] += min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])

                if matrix[r][c] > max_len:
                    max_len = matrix[r][c]

        return max_len ** 2


s = Solution()
print(s.maximalSquare2(matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                               ["1", "0", "0", "1", "0"]]))
