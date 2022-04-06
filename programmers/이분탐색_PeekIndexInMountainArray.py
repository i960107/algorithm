from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    l, u = 1, len(arr) - 2
    # the comparison a[i] < a[i+1] looks like true,true,true,false,false,false.
    # first false is the summit
    while l <= u:
        mid = l + (u - l) // 2
        # 왼쪽 부분
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        elif arr[mid] > arr[mid + 1]:
            u = mid - 1

    return l


print(peakIndexInMountainArray(arr=[0, 1, 0]))  # 1
print(peakIndexInMountainArray(arr=[0, 2, 1, 0]))  # 1
print(peakIndexInMountainArray(arr=[0, 10, 5, 2]))  # 1
print(peakIndexInMountainArray(arr=[3, 4, 5, 1]))  # 2
