def solution(n: int) -> int:
    # dp 조기 return 조건 빼먹지 말기!
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    divisor = 1234567
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % divisor
    return dp[n]


print(solution(4))
print(solution(3))
