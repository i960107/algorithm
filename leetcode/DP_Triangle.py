from typing import List


# def pascal_triangle(num_rows: int) -> List[int]:
#     answer = [[1] * i for i in range(1, num_rows + 1)]
#
#     for i in range(1, num_rows):
#         for j in range(1, len(answer[i]) - 1):
#             answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]
#
#     return answer
#
#
# print(pascal_triangle(5))
# print(pascal_triangle(1))
#
#
# def pascal_triangle2(row_index: int) -> List[int]:
#     answer = [[1] * (i + 1) for i in range(row_index + 1)]
#
#     for i in range(1, row_index + 1):
#         for j in range(1, len(answer[i]) - 1):
#             answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]
#
#     return answer[row_index]
#
#
# print(pascal_triangle2(3))
# print(pascal_triangle2(0))
#
#
# def minimum_total_fail(triangle: List[List[int]]) -> int:
#     # 틀린 이유: 매번 둘 중에 작은 걸 선택하는 greedy 문제가 아님.
#     tot = triangle[0][0]
#
#     prev_j = 0
#     for i in range(1, len(triangle)):
#         tmp_v = 10001
#         tmp_j = -1
#
#         if 0 <= prev_j < len(triangle[i]) and triangle[i][prev_j] < tmp_v:
#             tmp_v, tmp_j = triangle[i][prev_j], prev_j
#
#         if 0 <= prev_j + 1 < len(triangle[i]) and triangle[i][prev_j + 1] < tmp_v:
#             tmp_v, tmp_j = triangle[i][prev_j + 1], prev_j + 1
#
#         tot += tmp_v
#         prev_j = tmp_j
#
#     return tot


def minimum_total(triangle: List[List[int]]) -> int:
    dp = [[0] * (len(triangle[i])) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if 0 < j < len(dp[i]) - 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]

    return min(dp[-1])


print(minimum_total(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimum_total(triangle=[[-10]]))
print(minimum_total(triangle=[[-1], [2, 3], [1, -1, -3]]))


def minimum_total2(triangle: List[List[int]]) -> int:
    dp = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
    return dp[0]


print(minimum_total2(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimum_total2(triangle=[[-10]]))
print(minimum_total2(triangle=[[-1], [2, 3], [1, -1, -3]]))


