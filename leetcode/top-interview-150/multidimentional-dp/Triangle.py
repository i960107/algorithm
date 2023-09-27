from typing import List


class Solution:
    # 왜 다이나믹 프로그래밍인가?
    # 최적 부분 구조. 중복된 하위 문제들
    # 각 칸까지의 minTotal경로를 저장해둔다. 다음 레벨에서 이전 레벨까지의 최소 경로를 선택한다.
    # 이전 레벨까지의 최소 경로는 중복된 하위문제로 이미 저장된 값을 사용한다.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c + 1])
        return triangle[0][0]


s = Solution()
print(s.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
