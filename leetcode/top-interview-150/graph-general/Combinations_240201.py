from typing import List
from itertools import combinations


class Solution:
    # def dfs(start: int):
    #     if len(path) == k:
    #         answer.append(path[::])
    #         return
    #     for num in range(start + 1, n + 1):
    #         path.append(start)
    #         dfs(num)
    #         path.pop()
    def combinations(self, n: int, k: int) -> List[List[int]]:
        answer = []
        path = []

        def dfs(start: int):
            # 같은 조합이 여러번 추가된다 [1,2]
            # 왜냐하면 이미 길이가 k가 된 후에도 이 후의 숫자들을 고려하기 때문에
            # [1,2,3] [1,2,4]조합이 고려되어 [1,2]가 두번 추가된다
            # 완성된 조합은 한번만 고려되도록. 넣고나서 길이를 비교한다.
            if len(path) == k:
                answer.append(path[::])
                return
            for num in range(start, n + 1):
                path.append(num)
                dfs(num + 1)
                path.pop()

        dfs(1)
        return answer

    def combinations2(self, n: int, k: int) -> List[List[int]]:
        return [list(x) for x in combinations(range(1, n + 1), k)]


s = Solution()
print(s.combinations(4, 2))
