import bisect
from typing import List


def checkIfExist(arr: List[int]) -> bool:
    # 0보다 작은 수도 있으므로 양방향으로 봐야 하나?
    arr.sort()
    for i, n in enumerate(arr):
        if n > 0:
            j = bisect.bisect_left(arr, n * 2, i + 1)
        else:
            j = bisect.bisect_left(arr, n * 2, 0, i - 1)

        if j < len(arr) and arr[j] == arr[i] * 2:
            return True
    # else:
    #     j = bisect.bisect_left(arr, n * 2, 0, i - 1)
    #     if j < len(arr) and arr[j] == arr[i] * 2:
    #         return True
    return False


print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([7, 1, 14, 11]))
print(checkIfExist([3, 1, 7, 11]))
print(checkIfExist([-10, 12, -20, -8, 15]))
