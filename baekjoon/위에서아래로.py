from typing import List


def solution(arr: List[int]) -> List[int]:
    '''use python sort library '''
    return sorted(arr, reverse=True)


def solution2(arr: List[int]):
    '''quick sort algorithm - asc'''

    def quicksort(arr, start, end):
        if start >= end:
            return
        pivot = start
        left, right = start + 1, end

        while left <= right:

            # 피벗보다 큰 데이터를 찾을때까지 반복
            while left <= end and arr[pivot] >= arr[left]:
                left += 1

            # 피벗보다 작은 데이터를 찾을때까지 반복
            while start < right and arr[right] >= arr[pivot]:
                right -= 1

            if left > right:
                arr[pivot], arr[right] = arr[right], arr[pivot]
            else:
                arr[left], arr[right] = arr[right], arr[left]

        quicksort(arr, start, right - 1)
        quicksort(arr, right + 1, end)

    quicksort(arr, 0, len(arr) - 1)


def solution3(arr: List[int]) -> List[int]:
    '''quick sort algorithm2 - 파이썬의 장점을 살린 퀵 정렬 '''
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return solution3(left) + [pivot] + solution3(right)


l = [15, 27, 12]
res = solution3(l)
print(res)
