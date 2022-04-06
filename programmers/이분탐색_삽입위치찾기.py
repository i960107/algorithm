import bisect
from typing import List


def serach_insert(nums: List[int], target: int) -> int:
    '''35.serach insert position'''
    l, u = 0, len(nums) - 1
    while l <= u:
        mid = l + (u - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            u = mid - 1
        else:
            return mid

    # 왜 return u ? target이 nums안에 존재하지 않을때
    return u + 1


print(serach_insert([1, 3, 5, 6], 5))
print(bisect.bisect_left([1, 3, 5, 6], 5))

# 삽입할 위치 앞. 가장 가까운 작은 값에 right
# left : 0  right: 0
print(serach_insert([1, 3, 5, 6], 2))
print(bisect.bisect_left([1, 3, 5, 6], 2))

# left : 2  right: 1
print(serach_insert([1, 3, 5, 6], 4))
print(bisect.bisect_left([1, 3, 5, 6], 4))  # 2

# left : 3  right: 3
print(serach_insert([1, 3, 5, 6], 7))
print(bisect.bisect_left([1, 3, 5, 6], 7))
