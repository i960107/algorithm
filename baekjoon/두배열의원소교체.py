from typing import List


def solution(arr1: List[int], arr2: List[int], k) -> int:
    arr1.sort()
    arr2.sort(reverse=True)

    pos1 = 0
    pos2 = 0
    while k != 0:
        if arr1[pos1] >= arr2[pos2]:
            break
        arr1[pos1], arr2[pos2] = arr2[pos2], arr1[pos1]
        pos1 += 1
        pos2 += 1
        k -= 1
    return sum(arr1)


print(solution([1, 2, 5, 4, 3], [5, 5, 6, 6, 5], 3))
