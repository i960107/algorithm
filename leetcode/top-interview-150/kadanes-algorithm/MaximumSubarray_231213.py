from typing import List


class Solution:
    # kadane's algorithm
    # prefix sum
    # can subarray be empty?
    def maxSubArray(self, nums: List[int]) -> int:
        # min_prefix = nums[0] 아님.
        # min_prefix의 최대값은 empty subarray. min_prefix >0 일 경우 빼주지 않는게 best sum에 이득.
        min_prefix = 0
        prefix = 0
        ans = float('-INF')
        for i in range(len(nums)):
            # 1. 자기 자신까지 합 prefix 구하기.
            prefix += nums[i]
            # 2. best sum 구하기. 자기 이전까지의 min_prefix와의 diff.
            if prefix - min_prefix > ans:
                ans = prefix - min_prefix
            # 3. 자기 자신 포함한 min_prefix 갱신하기.
            if prefix < min_prefix:
                min_prefix = prefix

        return ans


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([5, 4, -1, 7, 8]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([-2, -1]))
print(s.maxSubArray([-2, 1]))
