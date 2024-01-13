import bisect
from typing import List


class Solution:
    # strictly increasing subsequence
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        # dp[i] : 0 ~ i까지 범위의 subarray중 i번째 원소를 반드시 포함하는 strictly increasing subarray length의 최대값
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(i):
                # 반드시 i번째 원소를 포함해야함.
                # if nums[j] > nums[i] and dp[j] > dp[i]:
                #     dp[i] = dp[j] -> global 최대값을 췆ㄱ하고 있음.
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > max_len:
                max_len = dp[i]
        print(dp)
        return max_len

    def lengthOfLIS2(self, nums: List[int]) -> int:
        result = []
        for n in nums:
            if not result or result[-1] < n:
                result.append(n)
            else:
                pos = bisect.bisect_left(result, n)
                result[pos] = n
        return len(result)


s = Solution()
print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(s.lengthOfLIS(nums=[4, 10, 4, 3, 8, 9]))  #
print()
print(s.lengthOfLIS2(nums=[10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(s.lengthOfLIS2(nums=[4, 10, 4, 3, 8, 9]))  #
