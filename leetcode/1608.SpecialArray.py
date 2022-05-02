import bisect
from typing import List


def specialArray(nums: List[int]) -> int:
    if not nums:
        return 0
    prev_index = 0
    nums.sort()
    for x in range(1, len(nums) + 1):
        index = bisect.bisect_left(nums, x, prev_index)
        if len(nums) - index == x:
            return x
        prev_index = index
    return -1


print(specialArray([3, 5]))
print(specialArray([0, 0]))
print(specialArray([0, 4, 3, 0, 4]))
