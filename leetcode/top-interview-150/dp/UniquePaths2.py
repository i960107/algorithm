from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 시작 시점에 장애물 있을 수 있음.
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        # 아 시발...
        for c in range(1, n):
            if obstacleGrid[0][c] == 1:
                obstacleGrid[0][c] = 0
            else:
                obstacleGrid[0][c] = obstacleGrid[0][c - 1]
        for r in range(1, m):
            if obstacleGrid[r][0] == 1:
                obstacleGrid[r][0] = 0
            else:
                obstacleGrid[r][0] = obstacleGrid[r - 1][0]

        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
        print(obstacleGrid)
        return obstacleGrid[m - 1][n - 1]


s = Solution()
# print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
# print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
