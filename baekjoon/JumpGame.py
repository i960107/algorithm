from typing import List


def jump(nums: List[int]) -> int:

    dp = [len(nums) + 1] * len(nums)
    dp[0] = 0

    for i in range(len(dp)):
        for j in range(1, nums[i] + 1):
            if i + j >= len(nums):
                continue
            dp[i + j] = min(dp[i + j], dp[i] + 1)

    return dp[-1]


print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))
