from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        # 값, 인덱스
        # 이전값들중 최대값
        maxH = [[0, 0] for _ in range(n)]
        maxH[0] = [height[0], 0]
        for i in range(1, n):
            if height[i] > maxH[i - 1][0]:
                maxH[i] = [height[i], i]
            else:
                maxH[i] = maxH[i - 1]

        for i in range(1, n):
            if maxH[i-1][0] < height[i]:
            else:
                height[i]


s = Solution()
print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea(height=[1, 1]))
