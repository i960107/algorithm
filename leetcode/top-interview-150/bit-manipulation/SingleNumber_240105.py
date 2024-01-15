from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
            print("result", result)
        return result


s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([2, 1, 1]))
