from typing import List


# O(M + LogN)
# 열에 대해서도 이진탐색 가능. 오름차순을 정렬된 배열에서 target보다 크거나 같은 원소 중 최소값을 찾는 것.
def solution(matrix: List[List[int]], target: int) -> bool:
    r = 0
    while r < len(matrix) and matrix[r][-1] < target:
        r += 1
    if r == len(matrix):
        return False

    start = 0
    end = len(matrix[r])

    while start <= end:
        mid = (start + end) // 2
        if matrix[r][mid] == target:
            return True
        elif matrix[r][mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


def solution2(matrix: List[List[int]], target: int) -> bool:
    low_r = 0
    hi_r = len(matrix) - 1

    r = None
    while low_r <= hi_r:
        mid = (low_r + hi_r) // 2
        if matrix[mid][-1] >= target:
            r = mid
            hi_r = mid - 1
        else:
            low_r = mid + 1

    if r is None:
        return False

    low_c = 0
    hi_c = len(matrix[r]) - 1

    while low_c <= hi_c:
        mid = (low_c + hi_c) // 2
        if matrix[r][mid] == target:
            return True
        elif matrix[r][mid] < target:
            low_c = mid + 1
        else:
            hi_c = mid - 1

    return False


print(solution([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(solution(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
print(solution(matrix=[[1], [2]], target=1))
print(solution(matrix=[[1], [2]], target=3))
print(solution(matrix=[[-100, -98, -97], [-1, 0, 1]], target=0))

print()

print(solution2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(solution2(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
print(solution2(matrix=[[1], [2]], target=1))
print(solution2(matrix=[[1], [2]], target=3))
print(solution2(matrix=[[-100, -98, -97], [-1, 0, 1]], target=0))
