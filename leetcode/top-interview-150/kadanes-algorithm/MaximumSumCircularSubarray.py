from typing import List


class Solution:
    # nonempty subarray
    #
    # def maxSubarraySumCircular(self, nums: List[int]) -> int:
    #     prefix = [n for n in nums]
    #     max_sum = float('-INF')
    #     for i in range(1, len(nums)):
    #         if prefix[i - 1] > 0:
    #             prefix[i] += prefix[i - 1]
    #         if prefix[i] > max_sum:
    #             max_sum = prefix[i]
    #
    #     postfix = [n for n in nums]
    #     for i in range(len(nums) - 2, -1, -1):
    #         if postfix[i + 1] > 0:
    #             postfix[i] += postfix[i + 1]
    #         if postfix[i] > max_sum:
    #             max_sum = postfix[i]
    #
    #     # O (N^2 안될텐데..)
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if prefix[i]
    #
    #     print(dp)
    #     return max(dp)
    #
    # 누적합의 최대값
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # what if every value in array is negative?
        # global max  < 0 이라면 all value is negative
        cur_max, global_max = 0, nums[0]
        cur_min, global_min = 0, nums[0]

        total = 0

        for n in nums:
            total += n
            if cur_max > 0:
                cur_max += n
            else:
                cur_max = n
            if cur_max > global_max:
                global_max = cur_max

            if cur_min < 0:
                cur_min += n
            else:
                cur_min = n
            if cur_min < global_min:
                global_min = cur_min

        if total == global_min:
            return global_max
        return max(global_max, total - global_min)


s = Solution()
print(s.maxSubarraySumCircular([-3, -2, -3]))
print(s.maxSubarraySumCircular([5, -3, 5]))
print(s.maxSubarraySumCircular([5, 3, 5]))
print(s.maxSubarraySumCircular([1, -1]))
print(s.maxSubarraySumCircular([1]))
print(s.maxSubarraySumCircular([1, -2, 3, -2]))
