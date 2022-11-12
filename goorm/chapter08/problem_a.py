from typing import List


def solution_a(arr):
    '''재귀 풀이 memoization'''
    # n은 숫자의 개수
    n = len(arr) // 2 + 1
    MIN_INF = float("INF")
    MAX_INF = float("-INF")
    # dp[i][j] := arr[i...j]를 계산한 최솟값, 최대값
    # 틀림
    # memo = [[[MIN_INF, MAX_INF]] for _ in range(n) for _ in range(n)]
    memo = [[[MIN_INF, MAX_INF]] * n for _ in range(n)]

    def _solution(left_most, right_most):
        if left_most < 0 or right_most >= len(arr) or left_most > right_most:
            return 0

        elif left_most == right_most:
            memo[left_most // 2][right_most // 2] = [int(arr[left_most]), int(arr[right_most])]
            return [int(arr[left_most]), int(arr[right_most])]

        elif memo[left_most // 2][right_most // 2] != [MIN_INF, MAX_INF]:
            return memo[left_most // 2][right_most // 2]

        answer = [MIN_INF, MAX_INF]

        for mid in range(left_most, right_most, 2):

            left_res = _solution(left_most, mid)
            right_res = _solution(mid + 2, right_most)

            min_res = MIN_INF
            max_res = MAX_INF
            if arr[mid + 1] == "+":
                min_res, max_res = left_res[0] + right_res[0], left_res[1] + right_res[1]
            else:
                min_res, max_res = left_res[0] - right_res[1], left_res[1] - right_res[0]
            answer[0] = min(answer[0], min_res)
            answer[1] = max(answer[1], max_res)

        memo[left_most // 2][right_most // 2] = answer

        return answer

    res = _solution(0, len(arr) - 1)
    return res[1]


def solution_b(arr: List[str]) -> int:
    '''반복문 풀이 tabulation- solution_a보다 약 2배 빠름'''
    # l : 배열 arr의 길이
    # n : 배열 arr에 속한 숫자의 개수
    l, n = len(arr), len(arr) // 2 + 1
    INF = float("INF")
    min_dp = [[INF] * n for _ in range(n)]
    max_dp = [[-INF] * n for _ in range(n)]

    for i in range(n):
        min_dp[i][i] = int(arr[i * 2])
        max_dp[i][i] = int(arr[i * 2])

    for c in range(1, n):
        for i in range(n - c):
            j = i + c
            for k in range(i, j):
                if arr[k * 2 + 1] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])

    return int(max_dp[0][n - 1])


#print(solution_b(["1", "-", "3", "+", "5", "-", "8"]))
res  = ([["a", "b"] for _ in range(5) for _ in range(5)])
print(len(res))
