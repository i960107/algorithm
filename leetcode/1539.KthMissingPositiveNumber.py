from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        diff = arr[mid] - mid - 1
        if diff >= k:
            l = mid - 1
        else:
            l = mid + 1
        return arr[r] + (k - (arr[r] - r - 1))
