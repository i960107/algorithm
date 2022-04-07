import bisect
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    '''투포인터'''
    l, r = 0, len(numbers) - 1
    # 같을때는 치지 않음
    while l < r:
        if numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            return [l + 1, r + 1]


print(twoSum(numbers=[2, 7, 11, 15], target=9))  # [1,2]
print(twoSum(numbers=[2, 3, 4], target=6))  # [1,3]
print(twoSum(numbers=[-1, 0], target=-1))  # [1,2]


def twoSumBinarySearch(numbers: List[int], target: int) -> List[int]:
    '''이진검색'''
    # ONlogN 느림
    for k, v in enumerate(numbers):
        l, r = k + 1, len(numbers) - 1
        expected = target - v
        while l <= r:
            mid = l + (r - l) // 2
            if numbers[mid] < expected:
                l += 1
            elif numbers[mid] > expected:
                r -= 1
            else:
                return [k + 1, mid + 1]


print(twoSumBinarySearch(numbers=[2, 7, 11, 15], target=9))  # [1,2]
print(twoSumBinarySearch(numbers=[2, 3, 4], target=6))  # [1,3]
print(twoSumBinarySearch(numbers=[-1, 0], target=-1))  # [1,2]


def twoSumBisect(numbers: List[int], target: int) -> List[int]:
    '''이진검색'''
    # ONlogN 느림
    for k, v in enumerate(numbers):
        expected = target - v
        index = bisect.bisect_left(numbers, expected, k + 1)
        if index < len(numbers) and numbers[index] == expected:
            return [k + 1, index + 1]


print(twoSumBisect(numbers=[2, 7, 11, 15], target=9))  # [1,2]
print(twoSumBisect(numbers=[2, 3, 4], target=6))  # [1,3]
print(twoSumBisect(numbers=[-1, 0], target=-1))  # [1,2]
