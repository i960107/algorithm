import bisect
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    left = bisect.bisect_left(nums, target)
    if left < len(nums) and nums[left] == target:
        right = left
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]
    else:
        return [-1, -1]


print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(searchRange(nums=[], target=0))
