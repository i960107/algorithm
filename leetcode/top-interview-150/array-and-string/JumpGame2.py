from typing import List


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



s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
