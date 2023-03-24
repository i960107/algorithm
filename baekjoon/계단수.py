from collections import defaultdict


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

    # print([i for row in dp[n] for i, x in enumerate(row) if x != 0])
    # print(sum([x for row in dp[n] for i, x in enumerate(row) if x != 0]))
    answer = 0
    bitmask = (1 << 10) - 1
    # 1부터 더해주어야함.
    for end in range(10):
        answer += dp[n][end][bitmask]
        answer %= divisor

    return answer


def solution2(n: int):
    dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n + 1)]

    max = 1000000000
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


def solution3(n: int):
    # dp 초기화 주의
    dp = [[defaultdict(int) for _ in range(10)] for _ in range(n + 1)]
    dp[1][0][0] = 0
    divisor = 1000000000
    for end in range(1, 10):
        dp[1][end][1 << end] = 1

    for number_of_digit in range(1, n):
        # 이전 자리수의 end
        # 뒤로 더해주는거 가능?
        # dict에는 삽입된 순서가 유지 되기 때문에, 뒤로 더해주면 dict가 뒤죽박죽임.
        for end in range(10):
            items = dp[number_of_digit][end].items()
            for bit, count in items:
                if end > 0:
                    dp[number_of_digit + 1][end - 1][bit | (1 << (end - 1))] += dp[number_of_digit][end][bit]
                if end < 9:
                    dp[number_of_digit + 1][end + 1][bit | (1 << (end + 1))] += dp[number_of_digit][end][bit]

    answer = 0
    for end in range(10):
        answer += dp[n][end][(1 << 10) - 1]
        answer %= divisor
    return answer


n = int(input())
# print(solution(n))
# # print()
# print(solution2(n))
print(solution3(n))
