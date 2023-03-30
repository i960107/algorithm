from typing import List


def solution_fail(board: List[List[int]], skills: List[List[int]]) -> int:
    n, m = len(board), len(board[0])
    affected = [[0] * m for _ in range(n)]
    ATTACK = 1
    DEFENSE = 2
    # 행만 누적합 사용하는 것도 250,000 * 1,000 시간 초과!
    for type, r1, c1, r2, c2, degree in skills:
        for r in range(r1, r2 + 1):
            affected[r][c1] += degree * -1 if type == ATTACK else degree
            if c2 + 1 < m:
                affected[r][c2] += degree * 1 if type == ATTACK else degree * -1
    for r in range(n):
        for c in range(m):
            pass


def solution(board: List[List[int]], skills: List[List[int]]) -> int:
    n, m = len(board), len(board[0])
    affected = [[0] * m for _ in range(n)]
    ATTACK = 1
    DEFENSE = 2
    # 행만 누적합 사용하는 것도 250,000 * 1,000 시간 초과!
    for type, r1, c1, r2, c2, degree in skills:
        affected[r1][c1] += (degree if type == DEFENSE else degree * -1)
        if c2 + 1 < m:
            affected[r1][c2 + 1] += (degree * -1 if type == DEFENSE else degree)
        if r2 + 1 < n:
            affected[r2 + 1][c1] += (degree * -1 if type == DEFENSE else degree)
        if r2 + 1 < n and c2 + 1 < m:
            affected[r2 + 1][c2 + 1] += (degree if type == DEFENSE else degree * -1)

    # test = [[0] * m for _ in range(n)]
    # for type, r1, c1, r2, c2, degree in skills:
    #     for r in range(r1, r2 + 1):
    #         for c in range(c1, c2 + 1):
    #             if type == ATTACK:
    #                 test[r][c] -= degree
    #             else:
    #                 test[r][c] += degree
    #
    # print("test")
    # for row in test:
    #     print(row)

    for r in range(n):
        for c in range(m):
            if r - 1 >= 0:
                affected[r][c] += affected[r - 1][c]
            if c - 1 >= 0:
                affected[r][c] += affected[r][c - 1]
            if r - 1 >= 0 and c - 1 >= 0:
                affected[r][c] -= affected[r - 1][c - 1]
    count = 0
    for r in range(n):
        for c in range(m):
            board[r][c] += affected[r][c]
            if board[r][c] > 0:
                count += 1
    return count


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
