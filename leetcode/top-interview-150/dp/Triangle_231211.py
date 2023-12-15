from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                left, right = triangle[r + 1][c], triangle[r + 1][c + 1]
                triangle[r][c] += (left if left < right else right)
        return triangle[0][0]


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
