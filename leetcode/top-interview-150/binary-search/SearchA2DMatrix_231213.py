from typing import List


class Solution:
    # O(Log(M*N)) = O(LogM + LogN)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        lo, hi = 0, len(matrix) - 1
        # 여기도 이진 탐색 가능.
        r = m
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][-1] >= target:
                r = mid
                hi = mid - 1
            else:
                lo = mid + 1

        if r == m:
            return False

        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[r][mid] > target:
                hi = mid - 1
            elif matrix[r][mid] < target:
                lo = mid + 1
            else:
                return True
        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
