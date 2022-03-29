from typing import List


def solution(n: int) -> List[int]:
    result = [[None] * i for i in range(1, n + 1)]

    i, j = -1, 0  # i는 행 j는 열을 나타냄(1~n). j <= i
    num = 1
    phase = 1
    while n > 0:
        if phase == 1:
            for _ in range(n):
                i += 1
                result[i][j] = num
                num += 1
        elif phase == 2:
            for _ in range(n):
                j += 1
                result[i][j] = num
                num += 1
        else:
            for _ in range(n):
                i -= 1
                j -= 1
                result[i][j] = num
                num += 1
        n -= 1
        phase = (phase + 1) % 3

    # 2차원 배열을 1차원 배열로 합치기
    # answer = []
    # for x in result:
    #     answer += x
    return sum(result, [])


def solution_others(n: int) -> List[int]:
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n + 1)]

    for i in range(n):
        for _ in range(n - i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
        
    return sum(board, [])


print(solution(4))
print(solution(5))
print(solution(6))
