from typing import List, Optional
import bisect


def solution(n: int, target: int, numbers: List[int]) -> int:
    left = get_left(target, numbers)
    if left == -1:
        return -1
    right = get_right(target, numbers, left, len(numbers))
    return right - left + 1


def get_left(target: int, numbers: List[int]) -> int:
    lo, hi = 0, len(numbers) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if (mid == 0 or numbers[mid - 1] != target) and numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def get_right(target: int, numbers: List[int], lo: int = 0, hi: Optional[int] = None) -> int:
    if hi is None:
        hi = len(numbers)

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if (mid == len(numbers) - 1 or numbers[mid + 1] != target) and numbers[mid] == target:
            return mid

        if numbers[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def solution2(n: int, target: int, numbers: List[int]) -> int:
    left = bisect.bisect_left(numbers, target)
    if left == n or numbers[left] != target:
        return -1
    right = bisect.bisect_right(numbers, target, left)
    return right - left


print(solution(7, 2, [1, 1, 2, 2, 2, 2, 3]))
print(solution2(7, 2, [1, 1, 2, 2, 2, 2, 3]))
print(solution(7, 4, [1, 1, 2, 2, 2, 2, 3]))
print(solution2(7, 4, [1, 1, 2, 2, 2, 2, 3]))
