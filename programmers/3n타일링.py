#통과는 됨. 최선?
def solution(n: int) -> int:
    if n == 1 or n == 3:
        return 0
    if n == 2:
        return 3

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0

    divisor = 1000000007
    for i in range(n + 1):
        for even in range(4, n + 1, 2):
            if i + even > n:
                break
            dp[i + even] += dp[i] * 2
            dp[i + even] %= divisor
        if i + 2 > n:
            break
        dp[i + 2] += dp[i] * 3
        dp[i + 2] %= divisor
    return dp[n]


print(solution(4))
