from typing import List


def solution(n: int) -> List[int]:
    result = [[None] * i for i in range(1, n + 1)]

    i, j = 1, 1  # i는 행 j는 열을 나타냄(1~n). j <= i
    num = 1
    while True:
        if i < n:
            i += 1
            result[i - 1][j - 1] = num
        else:
            if j < i:
                j += 1
                result[i - 1][j - 1] = num
            else:
                i -= 1
                result[i - 1][j - 1] = num
        num += 1

    # 2차원 배열을 1차원 배열로 합치기
    # answer = []
    # for x in result:
    #     answer += x
    return sum(result, [])


print(solution(4))
print(solution(5))
print(solution(6))
