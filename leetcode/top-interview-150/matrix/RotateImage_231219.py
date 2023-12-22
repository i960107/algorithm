from collections import deque
from typing import List


class Solution:
    # 정사각형일때와 직사각형일때 다름.
    def rotate_Fail(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # n -1 크기의 덱 활용?
        queue = deque()
        for i in range(n - 1):
            queue.append(matrix[0][i])
        dr = (1, 0, -1, 0)
        dc = (0, -1, 0, 1)

        i, j = 0, n - 1
        d = 0
        # (3,3,3,2)
        for count in range(n - 1, -1, -1):
            for k in range(3):
                for _ in range(count):
                    queue.append(matrix[i][j])
                    matrix[i][j] = queue.popleft()
                    i, j = i + dr[k], j + dc[k]
            print(i, j, matrix[i][j])
            queue.append(matrix[i][j])
            matrix[i][j] = queue.popleft()
            i += 1

        for row in matrix:
            print(row)

    # reverse후 transposing 과 transposing후 reverse(rows become columns, columns becomes rows) 결과 같음.
    # 왼오 revsere and 위아래 reverse와 transosing은 다름
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        l, r = 0, n - 1
        # 위아래 revserse -> transpoing. transpose후 왼오 reverse
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # transpose
        # 반을 기준으로 뒤집기.
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 왼오 reverse 어려움 -> 위아래 reverse후 transpos가 나음.
        l, r = 0, n - 1
        while l < r:
            for i in range(n):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1
        return matrix


s = Solution()
print(s.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.rotate2(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print()
print(s.rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
print(s.rotate2(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
