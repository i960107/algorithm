from typing import List


def solution_53_maximum_subarray(nums: List[int]) -> int:
    dp = [0] * len(nums)
    max_sum = dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_sum = max(dp[i], max_sum)
    return max_sum


# print(solution_53_maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(solution_53_maximum_subarray([1]))
# print(solution_53_maximum_subarray([5, 4, -1, 7, 8]))


def solution_918_maximum_sum_circular_subarray(nums: List[int]) -> int:
    dp = [0] * len(nums)

    tot = 0
    best = 0

    for i in range(0, len(dp)):
        dp[i] = max(dp[i - 1] - nums[i] if i > 0 else -30001, -nums[i])
        tot += -nums[i]
        best = max(dp[i], best)

    return - tot + best if tot and -tot + best else max(nums)


print(solution_918_maximum_sum_circular_subarray([1, -1, 3, -1]))
print(solution_918_maximum_sum_circular_subarray([5, -3, 5]))
print(solution_918_maximum_sum_circular_subarray([-3, -2, -3]))

print(solution_918_maximum_sum_circular_subarray([1, -2, 3, -2]))
print(solution_918_maximum_sum_circular_subarray([-7, 1, 2, 7, -2, -5]))
