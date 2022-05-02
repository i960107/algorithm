from typing import List, Tuple


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[right]:
            # mid ~ right안에 min이 없다
            right = mid

        else:
            left = mid + 1

    return nums[left]


def findMin2(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    left, right = 0, len(nums) - 1
    # if the last element is greater than first element(non-decreasing array)
    # then there is no rotation
    if nums[left] < nums[right]:
        return nums[left]
    # binary search
    while left <= right:
        mid = left + (right - left) // 2
        # if the mid element is greater than its next
        # then mid + 1 is the smallest
        # list index out of range 위험?
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        # if the mid element value is greater than the 0th element
        # this means the least value is still some where to the right
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1


print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([11, 13, 15, 17]))
print(findMin([11]))

print(findMin2([3, 4, 5, 1, 2]))
print(findMin2([4, 5, 6, 7, 0, 1, 2]))
print(findMin2([11, 13, 15, 17]))
print(findMin2([11]))
