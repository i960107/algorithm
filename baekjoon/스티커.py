from typing import List


def solution(n: int, sticker: List[List[int]]) -> int:
    # 각 칸을 마지막으로 골랐을때 점수의 최댓값
    dp = [[0] * n for _ in range(2)]
    i = 1
    # 스티커를 고르는 경우
    # 1) 2개 열을 건너띄는 경우는 없다
    # 2) 한 개 열을 건너띄는 경우 반드시 행을 바꾼다
    # 3개열을 기준으로 살펴보기

    # 첫 두 열은 따로 처리해주기!
    for i in range(2):
        dp[i][0] = sticker[i][0]
        if n > 1:
            # ^ 비트연산자 0 XOR 1 = 1 1 XOR 1 = 0. 다르면 1
            # i가 0이면 1, i가 1이면 0
            dp[i][1] = sticker[i ^ 1][0] + sticker[i][1]

    # 위,아래 다음열 위, 아래 순으로 탐색하기
    for j in range(2, n):
        for i in range(2):
            dp[i][j] = max(dp[i ^ 1][j - 2], dp[i ^ 1][j - 1]) + sticker[i][j]
    return max(dp[0][n - 1], dp[1][n - 1])


n = int(input())
sticker = []
for _ in range(2):
    sticker += list(map(int, input().split()))

print(solution(n, sticker))
