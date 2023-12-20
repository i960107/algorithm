from typing import List


class Solution:
    # 어떻게 하는게 가장 좋지?
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dc = (1, 0, -1, 0)
        dr = (0, 1, 0, -1)

        i, j, k = 0, 0, 0
        answer = []

        def isInRange(r: int, c: int) -> bool:
            return (0 <= r < m) and (0 <= c < n)

        while len(answer) < m * n:
            answer.append(matrix[i][j])
            matrix[i][j] = None
            nr, nc = i + dr[k], j + dc[k]
            if not isInRange(nr, nc) or matrix[nr][nc] is None:
                k = (k + 1) % len(dr)
                nr, nc = i + dr[k], j + dc[k]
            i, j = nr, nc
        return answer


s = Solution()
print(s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(s.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
