from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        LEFT = '('
        RIGHT = ')'

        answer = []

        # left, right를 outer scope variable로 관리할 수 있지만 코드를 알아보기가 어려움..
        # path별로 가지고 있는게 좋지 않을까?
        path = []
        left = right = 0

        def dfs():
            nonlocal left, right
            if left == right == n:
                answer.append(''.join(path))
                return

            if left < n:
                left += 1
                path.append(LEFT)
                dfs()
                path.pop()
                left -= 1
            if right < left:
                right += 1
                path.append(RIGHT)
                dfs()
                path.pop()
                right -= 1

        dfs()
        return answer


s = Solution()
print(s.generateParenthesis(3))
