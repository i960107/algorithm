from typing import List


# 배열이 정렬되어있는 경우에도 비교가 계속되는 문제 최적화하기!
def sort(arr: List[int]):
    for i in range(len(arr)):
        hasSwapped = False
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                hasSwapped = True
        if not hasSwapped:
            break
    return arr


print(sort([2, 3, 41, 23, 39, 21, 37, 16, 41, 10, 47, 12, 24]))
print(sort([2]))
print(sort([1, 2, 3, 4]))
