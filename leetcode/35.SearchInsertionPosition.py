from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    l, u = 0, len(nums) - 1

    while l <= u:
        mid = l + (u - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            u = mid - 1
        else:
            return mid
    return u + 1


print(searchInsert(nums=[1, 3, 5, 6], target=5))
print(searchInsert(nums=[1, 3, 5, 6], target=2))
print(searchInsert(nums = [1, 3, 5, 6], target = 7))
