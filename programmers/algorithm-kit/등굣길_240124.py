from typing import List


# 예쁘게 코드 짜는 방법.
# -> dp[0][1]혹은 dp[1][0]과 같이 시작점에 영향을 끼칠 수 있는 곳 중 한 곳에 1를 넣는다.
# 효율성 테스트 실패?
def solution(m: int, n: int, puddles: [List[List[int]]]) -> int:
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][1] = 1
    for c, r in puddles:
        dp[r][c] = -1
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if dp[r][c] == -1:
                dp[r][c] = 0
                continue
            # modulo operation이 어떻게 중간에 들어가도 되지?
            dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % 1000000007

    for row in dp:
        print(row)

    return dp[n][m]


print(solution(4, 3, [[2, 2]]))
print(solution(4, 3, [[2, 1]]))
print(solution(1, 3, [[1, 2]]))
print(solution(3, 1, [[2, 1]]))
