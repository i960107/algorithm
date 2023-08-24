class Solution(object):
    def remove_element(self, nums, val):
        EMPTY = 101
        k = 0
        for index, num in enumerate(nums):
            if num == val:
                nums[index] = EMPTY
            else:
                k += 1
        nums.sort()
        return k

    def remove_element2(self, nums, val):
        index = 0
        # index <= i
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


s = Solution()
print(s.remove_element([3, 2, 2, 3], 3))
print(s.remove_element2([3, 2, 2, 3], 3))
