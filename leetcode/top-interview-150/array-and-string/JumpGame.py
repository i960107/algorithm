from typing import List


class Solution:
    def canJump(self, nums: List[int]):
        if nums[0] == 0:
            return False
        for i in range(1, len(nums) - 1):
            if nums[i - 1] - 1 > nums[i]:
                nums[i] = nums[i - 1]
            if nums[i] == 0:
                return False
        return True

    def canJump(self, nums: List[int]):
        goal = len(nums) - 1

        curr = len(nums) - 2

        while curr >= 0:
            if curr + nums[curr] >= goal:
                goal = curr
            curr -= 1

        return goal == 0


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
print(s.canJump([0, 1]))
print(s.canJump([1, 0]))
