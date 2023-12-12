from typing import List


class Solution:
    def maxArea(self, nums: List[int]):
        left, right = 0, len(nums) - 1
        answer = 0
        while left < right:
            if nums[left] <= nums[right]:
                water = nums[left] * (right - left)
                left += 1
            else:
                water = nums[right] * (right - left)
                right -= 1
            if water > answer:
                answer = water
        return answer


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
