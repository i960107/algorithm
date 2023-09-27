from typing import List


class Solution:
    # greedy와 dp의 차이?
    # 둘다 최적 부분 구조를 찾아간다는 점에서 greedy라고 볼 수 있지 않나?
    # 그리디 항상 그순간에 최적이라고 생각되는 것을 선택하면서 풀이
    # 중복된 하위문제들에 대해서 최적해를 저장해두었다가 전체 최적해를 구한다
    # 다익스트라 알고리즘은 항상 최단 경로를 찾고 탐욕 선택 속성을 갖는 그리디 알고리즘이면서,
    # 이미 계산한 경로는 저장해두었다가 활용해 중복된 하위 문제들을 푸는 다이나믹 알고리즘이다.
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[m - 1][n - 1]


s = Solution()
print(s.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
