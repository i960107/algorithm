from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # 행,렬 100개이므로 선형 검색 충분히 가능
    row = 0
    for row in range(len(matrix)):
        if matrix[row][-1] < target:
            continue
        else:
            break

    l, u = 0, len(matrix[row]) - 1
    while l <= u:
        mid = l + (u - l) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            l = mid + 1
        else:
            u = mid - 1
    return False


print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
