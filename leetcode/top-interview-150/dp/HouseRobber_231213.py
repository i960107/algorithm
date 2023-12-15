from typing import List


class Solution:
    def rob(self, nums: List[int]):
        # dp[i] 는 i번째 집까지 털 수 있는 최대 금액?
        if len(nums) < 3:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    def rob_fail(self, nums: List[int]):
        # dp[i] 는 i번째 집을 터는 경우의 최대 금액?
        # 최적 부분 구조로 쪼갤 수 없음.
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        # oxoxoxo경우박에 체크 못함?
        # 터는 경우의 최대값, 털지 않는 경우의 최대값 -> i번째 집까지 최대값
        for i in range(2, len(nums)):
            dp[i] = dp[i - 2] + nums[i]


s = Solution()
print(s.rob([1, 2]))
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([2, 1, 1, 2]))
