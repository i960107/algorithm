def get_all_possible_ways(N: int) -> int:
    dp = [[1] * (3 + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    # dp[i][j]를 그자리에 사람이 앉는 경우의 수로 할까? 정답이 뭐가 되지
    # dp[i][j]를 그자리에 사람이 앉든 안 앉든 모든 경우의 수로 한다면 -> dp[n-1][2]가 정답
    for i in range(1, N + 1):
        for j in range(1, 3 + 1):
            if i == j == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]
    for i in range(N + 1):
        print(dp[i])
    return dp[N - 1][2] % 100000007


N = int(input())
print(get_all_possible_ways(N))
