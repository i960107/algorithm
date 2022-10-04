from itertools import permutations


def solution(N: int, M: int, k: int) -> str:
    '''순열'''
    answer = ["z"] * (N + M)
    for i in sorted(permutations(range(N + M), N))[k - 1]:
        answer[i] = "a"
    return "".join(answer)

def solution_dfs(N: int, M: int, k: int) -> str:
    '''dfs'''
    def dfs(path:List[str],):
        pass

def solution_dp(N: int, M: int, k: int) -> str:
    '''dynamic programming'''

    #  dp를 2차원배열로 저장하면 어떤 글자가 행이되는지 주의해야함
    dp = [[-1] * M for _ in range(N)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if i + j == 0:
                dp[i][j] = 0

            elif i == 0 or j == 0:
                dp[i][j] = 1

            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    answer = []

    while True:

        if dp[N - 1][M] >= k:
            answer.append("a")
            N -= 1

        else:
            answer.append("z")
            M -= 1

    return answer


print(solution(2, 2, 2))
