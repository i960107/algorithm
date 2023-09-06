from typing import List


def sort(arr: List[int]):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(sort([2, 3, 41, 23, 39, 21, 37, 16, 41, 10, 47, 12, 24]))
