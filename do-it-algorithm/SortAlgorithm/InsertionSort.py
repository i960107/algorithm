from typing import List


def sort(arr: List[int]):
    result = []
    for n in arr:
        result.append(n)
        i = len(result) - 1
        while i > 0 and result[i] < result[i - 1]:
            result[i], result[i - 1] = result[i - 1], result[i]
            i -= 1
    return result


def sortInPlace(arr: List[int]):
    for i in range(1, len(arr)):
        curr = arr[i]
        p = i - 1
        while p >= 0 and arr[p] > curr:
            arr[p + 1] = arr[p]
            p -= 1
        arr[p + 1] = curr
    return arr


print(sort([2, 3, 41, 23, 39, 21, 37, 16, 41, 10, 47, 12, 24]))
print(sortInPlace([2, 3, 41, 23, 39, 21, 37, 16, 41, 10, 47, 12, 24]))
