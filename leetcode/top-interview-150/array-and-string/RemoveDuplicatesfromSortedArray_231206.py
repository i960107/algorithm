def removeDuplicates(nums):
    pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[pos] = nums[i]
            pos += 1
    return pos

# 어떤 풀이지?
# def removeDuplicates2(self, nums) -> int: i, j = 0, 1
#     k = 1
#     while j < len(nums):
#         if nums[j] > nums[i]:
#             i += 1
#             nums[i] = nums[j]
#             k += 1
#         j += 1
#
#     for index in range(i + 1, len(nums)):
#         nums[index] = None
#
#     return k
