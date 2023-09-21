from typing import List
from collections import deque


# 마지막 칸에 도달하기 위해 필요한 최소 점프수
# 마지막 칸에 도달하지 못하는 경우는 없다
# 매 칸마다 점프 가능한 칸수가 다르다
# 최대 1000칸을 뛰어넘을 수 있다.
# jump game 1과의 비교? 어려운 이유. 각 칸마다 뛸 수 있는 칸수가 랜덤함 1, 2칸으로 제한되는 것이 아님.

# 1) 방법1: 각 칸에 도달하기 위한 최소 점프수를 기록함. O(N^2)이라서 통과는 되지만 매우 느림..
# 2) dfs: 전체 탐색은 복잡도가 너무 높음.
class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = -1
        dp = [INF] * len(nums)
        dp[0] = 0

        for i, n in enumerate(nums):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and dp[i + j] == INF:
                    dp[i + j] = dp[i] + 1
        print(dp)
        return dp[-1]

    # def jump2(self, nums: List[int]) -> int:

    # [0]인 경우 주의

    # bfs - 최단거리
    # 넣으면서 확인하는게 빼면서 확인하는 것보다 훨씬 빠름...
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        queue = deque()
        queue.append((0, 0))

        visited = set()
        visited.add(0)

        while queue:
            curr, count = queue.popleft()

            for k in range(1, nums[curr] + 1):
                nxt, nxt_count = curr + k, count + 1

                if nxt in visited:
                    continue
                visited.add(nxt)

                if nxt == len(nums) - 1:
                    return nxt_count

                queue.append((nxt, nxt_count))

    # implicit BFS, greedy
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        # Implicit BFS
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:  # Visited all the items on the current level
                ans += 1  # Increment the level
                end = farthest  # Make the queue size for the next level

        return ans

    # dp memoization
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]

        def solve(arr, pos, n, c):
            if pos >= n - 1:
                dp[-1] = 0
                return c

            if dp[pos] != -1:
                return dp[pos] + c

            mini = 100000
            for i in range(1, arr[pos] + 1):
                if pos + i >= n:
                    break
                mini = min(solve(arr, pos + i, n, 1), mini)

            dp[pos] = mini
            return mini + c

        solve(nums, 0, n, 0)
        return dp[0]

    # 매번 최대로 점프하는 것이 좋다?
    def jump(self, nums: List[int]) -> int:

        x = [nums[i] + i for i in range(len(nums))]
        # each element in this represent max index that can be reached from the current index

        l, r, jumps = 0, 0, 0

        while r < len(nums) - 1:
            jumps += 1
            l, r = r + 1, max(x[l:r + 1])

        return jumps

    # dp
    # 왜 bfs보다 더 오래 걸릴까?
    def jump(self, nums: List[int]) -> int:
        INF = -1
        dp = [INF] * len(nums)
        dp[0] = 0

        for i, n in enumerate(nums):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums) or dp[i + j] != INF:
                    continue
                dp[i + j] = dp[i] + 1
                if i + j == len(nums) - 1:
                    return dp[i + j]
        return dp[-1]


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
