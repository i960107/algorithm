from typing import List


def sort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    p1 = p2 = 0
    result = []
    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            result.append(left[p1])
            p1 += 1
        else:
            result.append(right[p2])
            p2 += 1

    result += left[p1:]
    result += right[p2:]
    return result


print(sort([2, 3, 41, 23, 39, 21, 37, 16, 41, 10, 47, 12, 24]))
