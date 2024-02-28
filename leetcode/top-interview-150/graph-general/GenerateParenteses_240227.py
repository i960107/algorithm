from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        LEFT = "("
        RIGHT = ")"

        # 중복이 있을 수 있나? 없음.
        # )부터시작할 수 없음. left < right일 수 없음.
        # recursive.
        def dfs(left, right, result):
            if left + right == n * 2:
                answer.append(''.join(result))
                return

            if left < n:
                dfs(left + 1, right, result + [LEFT])
            # left > right
            if right < n and left >= right + 1:
                dfs(left, right + 1, result + [RIGHT])

        dfs(0, 0, [])
        return answer

    # left, right, result 변수를 바깥에 두고 queue를 사용해서 iterative하게 구현할 수 있음.
    def generateParenthesis2(self, n: int) -> List[str]:
        answer = []
        LEFT = '('
        RIGHT = ')'
        q = [(0, 0, '')]
        while q:
            left, right, s = q.pop()
            if left == right == n:
                answer.append(s)
                continue

            if left < n:
                q.append((left + 1, right, s + LEFT))

            if right < left:
                q.append((left, right + 1, s + RIGHT))
        return answer


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis2(3))
