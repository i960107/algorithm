from typing import List


# def solution(triangle: list) -> int:
#     # 계속해서 가장 큰 것을 선택해 가면 최댓값이 되나?
#     # 아님..현재 큰 값일지라도 다음 행에서 역전될 수 있음
#     # 매 행마다 합한 값 기록해서 더해가야.
#
#     for i in range(1, len(triangle)):
#         for j in range(len(triangle[i])):
#             left = triangle[i - 1][j - 1] if j > 0 else triangle[i - 1][j]
#             right = triangle[i - 1][j] if j < len(triangle[i - 1]) else left
#             triangle[i][j] += left if left >= right else right
#
#             # if (j + 1 >= len(triangle[i - 1])) or (
#             #         j + 1 < len(triangle[i - 1]) and triangle[i - 1][j] >= triangle[i - 1][j + 1]):
#             #     accumulated += triangle[i - 1][j]
#             # elif j + 1 <= len(triangle[i - 1] - 1) and triangle[i - 1][j] < triangle[i - 1][j - 1]:
#             #     accumulated += triangle[i - 1][j - 1]
#             #     triangle[i][j] += accumulated
#
#     return max(triangle[-1])


# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

def solution(triangle: List[List[int]]) -> int:
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][-1] += triangle[i - 1][-1]

    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
