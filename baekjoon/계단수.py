from collections import defaultdict

max = 1000000000


def solution(n: int) -> int:
    divisor = 1000000000
    dp = [[defaultdict(int) for _ in range(10)] for _ in range(n + 1)]
    for end in range(1, 10):
        dp[1][end][1 << end] = 1

    for n in range(2, n + 1):
        for end in range(10):
            for bitmask in range(1 << 10):
                if end > 0:
                    dp[n][end][bitmask | (1 << end)] += dp[n - 1][end - 1][bitmask]
                if end < 9:
                    dp[n][end][bitmask | (1 << end)] += dp[n - 1][end + 1][bitmask]
                dp[n][end][bitmask | (1 << end)] %= divisor

    print([i for row in dp[n] for i, x in enumerate(row) if x != 0])
    print(sum([x for row in dp[n] for i, x in enumerate(row) if x != 0]))
    answer = 0
    bitmask = (1 << 10) - 1
    # 1부터 더해주어야함.
    for end in range( 10):
        answer += dp[n][end][bitmask]
        answer %= divisor

    return answer


def solution2(n: int):
    dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n + 1)]

    for i in range(10):
        dp[1][i][1 << i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            for k in range(1 << 10):
                if j == 0:
                    dp[i][j][1 << j | k] += dp[i - 1][j + 1][k]
                elif j == 9:
                    dp[i][j][1 << j | k] += dp[i - 1][j - 1][k]
                else:
                    dp[i][j][1 << j | k] += dp[i - 1][j + 1][k]
                    dp[i][j][1 << j | k] += dp[i - 1][j - 1][k]
                dp[i][j][1 << j | k] %= max

    # print([i for row in dp[n] for i, x in enumerate(row) if x != 0])
    # print(sum([x for row in dp[n] for i, x in enumerate(row) if x != 0]))
    answer = 0
    for i in range(1, 10):
        answer += dp[n][i][(1 << 10) - 1]
        answer %= max
    return answer


n = int(input())
# print(solution(n))
# print()
print(solution2(n))
