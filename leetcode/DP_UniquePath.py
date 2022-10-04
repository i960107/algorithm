from typing import List


def unique_paths(m: int, n: int) -> int:
    grid = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[m - 1][n - 1]


def unique_paths_combinational(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    m -= 1
    n -= 1

    if m < n:
        m, n = n, m

    res = 1
    j = 1

    for i in range(m + 1, n + m + 1):
        res *= i
        res /= j
        j += 1

    return res


# print(unique_paths_combinational(3, 7))


def unique_path_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    if obstacle_grid[0][0] == 1:
        return 0

    obstacle_grid[0][0] = 1

    for i in range(1, len(obstacle_grid)):
        obstacle_grid[i][0] = int(obstacle_grid[i - 1][0] and not obstacle_grid[i][0])

    for j in range(1, len(obstacle_grid[0])):
        obstacle_grid[0][j] = int(obstacle_grid[0][j - 1] and not obstacle_grid[0][j])

    for i in range(1, len(obstacle_grid)):
        for j in range(1, len(obstacle_grid)):
            if obstacle_grid[i][j]:
                obstacle_grid[i][j] = 0
            else:
                obstacle_grid[i][j] = obstacle_grid[i - 1][j] + obstacle_grid[i][j - 1]

    return obstacle_grid[-1][-1]


# print(unique_path_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# print(unique_path_with_obstacles([[0, 1], [0, 0]]))
# print(unique_path_with_obstacles([[0]]))
# print(unique_path_with_obstacles([[1, 0]]))

def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

    return grid[m - 1][n - 1]


# print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
# print(min_path_sum([[1, 2, 3], [4, 5, 6]]))


def min_falling_path_sum(matrix: List[List[int]]) -> int:
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += min(matrix[i - 1][j - 1] if j - 1 >= 0 else 100 * 100 + 1,
                                matrix[i - 1][j],
                                matrix[i - 1][j + 1] if j + 1 < len(matrix[0]) else 100 * 100 + 1
            )

        for i in range(len(matrix)):
            print(matrix[i])
        return min(matrix[-1])

    print(min_falling_path_sum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    print(min_falling_path_sum(matrix=[[-19, 57], [-40, -5]]))
