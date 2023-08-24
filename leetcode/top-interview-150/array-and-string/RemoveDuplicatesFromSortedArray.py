class Solution(object):
    def removeDuplicates(self, nums):
        index = 1
        for i in range(1, len(nums)):
            if nums[index - 1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
