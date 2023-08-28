from typing import List


# target보다 크거나 같은 원소중 최소 원소의 인덱스를 찾아야함.
# 이진검색으로 정렬된 리스트에 삽입할 위치를 찾는 것.
# false, false, false, true ,true , true가 되는 첫번째 true를 찾는 것.
def solution(nums: List[int], target: int):
    lo, hi = 0, len(nums) - 1

    result = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            result = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return result if result is not None else len(nums)


# print(solution([1, 3, 5, 6, 5], 5))
# print(solution([1, 3, 5, 5, 6], 5))
# print(solution([1, 3, 5, 6], 2))
# print(solution([-1, 3, 5, 6], 0))
# print(solution([1, 3, 5, 6], 7))
print(solution([1, 3, 5, 6], 0))
