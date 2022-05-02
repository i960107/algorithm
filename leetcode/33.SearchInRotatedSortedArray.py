from typing import List


def search(nums: List[int], target: int) -> int:
    # 최소 원소 찾기 -> pivot
    l, u = 0, len(nums) - 1
    while l < u:
        mid = l + (u - l) // 2
        if nums[mid] > nums[u]:
            l = mid + 1
        else:
            u = mid

    pivot = l

    # 이진 탐색하기
    l, u = 0, len(nums) - 1
    while l <= u:
        mid = l + (u - l) // 2
        pivot_mid = (mid + pivot) % len(nums)
        if nums[pivot_mid] == target:
            return pivot_mid
        elif nums[pivot_mid] < target:
            l = mid + 1
        else:
            u = mid - 1
    return -1


def search_insertion_position(nums: List[int], target: int) -> int:
    l, u = 0, len(nums) - 1
    while l <= u:
        mid = l + (u - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            u = mid - 1
    # u + 1
    return l


print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(search(nums=[1], target=0))
# pivot = 0인 경우
print(search(nums=[1, 3], target=1))
print(search(nums=[3, 1], target=1))
