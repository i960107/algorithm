from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        path = []

        def dfs(start: int):
            if len(path) == k:
                answer.append(path[::])
                return

            for num in range(start, n + 1):
                path.append(num)
                dfs(num + 1)
                path.pop()

        dfs(1)
        return answer

    def combineFail(self, n: int, k: int) -> List[List[int]]:
        answer = []
        path = []

        def dfs(start: int):
            if len(path) == k:
                answer.append(path[::])
                return
            path.append(start)
            for num in range(start + 1, n + 1):
                dfs(num)
            path.pop()
        dfs(1)
        return answer


s = Solution()
print(s.combine(4, 2))
print(s.combineFail(4, 2))
