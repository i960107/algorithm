from __future__ import annotations

import math
from typing import List


def get_max(nums: List[int]) -> int | None:
    '''분할정복을 사용한 풀이'''
    if len(nums) == 1:
        return nums[0]

    # mid = len(nums) -1 // 2  recursion error 발생
    # 2개 있을때를 기준으로 1개 1개 나눠지려면 앞에 len(nums)//2개 -> slice end index 에들어가면 Index로 자동 변환됨
    # 쪼갰을때 빈 배열이 안됨 최소 원소 개수 1개.
    mid = len(nums) // 2

    left_max = get_max(nums[:mid])
    right_max = get_max(nums[mid:])

    return max(left_max, right_max)


print(get_max(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(get_max(nums=[1]))
print(get_max(nums=[5, 4, -1, 7, 8]))


def maxSubArray(nums: List[int]) -> int:
    '''divide and conquer'''

    # O(NlogN)
    def findMaxSubArray(nums, left, right):
        # base case - empty array
        if left > right:
            return -math.inf
        mid = left + (right - left) // 2
        curr = best_left_sum = best_right_sum = 0

        for i in range(mid - 1, left - 1, -1):
            curr += nums[i]
            best_left_sum = max(best_left_sum, curr)
        curr = 0
        for i in range(mid + 1, right + 1):
            curr += nums[i]
            best_right_sum = max(best_right_sum, curr)
        best_combined_sum = nums[mid] + best_left_sum + best_right_sum

        left_half = findMaxSubArray(nums, left, mid - 1)
        right_half = findMaxSubArray(nums, mid + 1, right)
        return max(best_combined_sum, left_half, right_half)

    return findMaxSubArray(nums, 0, len(nums) - 1)


def maxSubArrayDynamic(nums: List[int]) -> int:
    '''dynamic programming'''
    # O(N)
    dp = [num for num in nums]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)


print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray(nums=[1]))
print(maxSubArray(nums=[5, 4, -1, 7, 8]))

print(maxSubArrayDynamic(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArrayDynamic(nums=[1]))
print(maxSubArrayDynamic(nums=[5, 4, -1, 7, 8]))
