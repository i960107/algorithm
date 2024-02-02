from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        path = []

        # 중복조합. the same number may be chosen
        def dfs(pos: int, acc: int):
            if acc == target:
                # tuple이 아닌 generator가 됨.
                # result.add((x for x in path))
                result.add(tuple(x for x in path))
                return

            if acc > target:
                return

            for i in range(pos, len(candidates)):
                path.append(candidates[i])
                dfs(i, acc + candidates[i])
                path.pop()

        dfs(0, 0)
        return [list(x) for x in result]


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
