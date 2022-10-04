from typing import List


def rob(self, nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)

    def _rob(nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    return max(_rob(nums[:-1]), _rob(nums[1:]))


print(rob([2, 3, 2]) == 3)
print(rob([1, 2, 3, 1]) == 4)
print(rob([1, 2, 3]) == 3)
