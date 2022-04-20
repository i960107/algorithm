from typing import List


def solution_mine(arr: List[int]) -> int:
    l, u = 1, len(arr) - 2
    while l <= u:
        mid = l + (u - l) // 2
        if arr[mid - 1] < arr[mid]:
            if arr[mid] > arr[mid + 1]:
                return mid
            else:
                l = mid + 1
        else:
            u = mid - 1


def peekIndexInMountainArray(arr: List[int]) -> int:
    '''find the largest index i such that arr[i] < arr[i+1]'''
    l, u = 0, len(arr) - 1
    while l < u:
        mid = l + (u - l) // 2
        # index out of bound error  없나?
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            u = mid
            # l =  u 일때 빠져나옴. 처음으로 다음 원소랑 비교해서 값이 작아질때 빠져나옴
    return l


print(peekIndexInMountainArray(arr=[0, 1, 0]))
print(peekIndexInMountainArray(arr=[0, 2, 1, 0]))
print(peekIndexInMountainArray(arr=[0, 10, 5, 2]))
