from typing import List


# 시간 초과. O(N^2)
def solution_fail(sequence: List[int]) -> int:
    # 연속 펄스 부분 수열.
    # 1로 시작하는 펄스 부분 수열: sum_part_a
    # -1로 시작하는 펄스 부분 수열: sum_part_b
    max_sum = 0
    for start in range(len(sequence)):
        sum_part = sequence[start]
        for end in range(start, len(sequence)):
            # 짝수번째
            if start != end:
                if (end - start) % 2 == 0:
                    sum_part += sequence[end]
                # 홀수 번째
                else:
                    sum_part -= sequence[end]
            if sum_part > max_sum:
                max_sum = sum_part
    return max_sum


def solution_fail(sequence: List[int]) -> int:
    # dp문제
    sequence = [x if i % 2 == 0 else x * -1 for i, x in enumerate(sequence)]
    n = len(sequence)
    EMPTY = int(1e9)
    dp = [[EMPTY] * n for _ in range(n)]

    def _dp(start: int, end: int) -> int:

        if dp[start][end] != EMPTY:
            return dp[start][end]

        if start == end:
            dp[start][end] = sequence[start]
            return dp[start][end]

        mid = (start + end) // 2
        left = _dp(start, mid)
        right = _dp(mid + 1, end)
        result = left + right
        dp[start][end] = result
        return result

    _dp(0, n - 1)
    for row in dp:
        print(row)
    return max(dp[0][n - 1], dp[0][n - 1] * -1)

def solution(sequence: List[int]) -> int:
    answer = 0
    n = len(sequence)
    dp = [0] * n
    dp[0] = sequence[0]

    if n == 1:
        return max(dp[0] * -1, dp[0])
    else:
        for i in range(1, n,2):
            sequence[i] *= -1
        dp[0] =sequence[0]
        for i in range(1, n):
            dp[i] = max(sequence[i], sequence[i] + dp[i-1])
        answer = max(dp)


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
