from typing import List


def solution(triangle: List[List[int]]) -> int:
    n = len(triangle)
    for r in range(n - 2, -1, -1):
        for c in range(len(triangle[r])):
            triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])
    return triangle[0][0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
