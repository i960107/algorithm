import heapq
from typing import List


class Solution:
    # 최단거리 -> bfs
    # 넣으면서 확인하는게 빼면서 확인하는 것보다 훨씬 빠름
    def _jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        goal = len(nums) - 1

        queue = []
        queue.append((0, 0))
        visited = set()
        visited.add(0)

        while queue:
            curr_count, curr = heapq.heappop(queue)
            for j in range(1, nums[curr] + 1):
                nxt_count, nxt = curr_count + 1, curr + j
                # 인덱스 벗어나는 것 체크해주어야함.
                if nxt > goal or nxt in visited:
                    continue
                if nxt == goal:
                    return nxt_count
                visited.add(nxt)
                heapq.heappush(queue, (nxt_count, nxt))

    # 핵심 아이디어는 가장 먼저 도착한 경로가 최단 경로. 그 이후 다른 경로로 도착한다고 해도 고려할 필요 없음.
    # dp - tabulation
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] : i칸까지 도착하기 위한 최소 경로
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    break
                if dp[i + j] == -1:
                    dp[i + j] = dp[i] + 1
        return dp[-1]

    # dp - memoization
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] : i칸에서 마지막 칸까지 도착하는 최소 점프 수
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    break
                if dp[i + j] == -1:
                    dp[i + j] = dp[i] + 1
        return dp[-1]


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
print(s.jump([0]))
print(s.jump([1]))
print(s.jump([10, 1, 1, 1, 1, 1, 1, 1]))
