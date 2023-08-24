class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        mid = len(nums) // 2
        if nums[mid] == nums[-1]:
            return nums[-1]
        else:
            return nums[0]


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([3]))
print(s.majorityElement([2, 2, 1, 1, 2]))
