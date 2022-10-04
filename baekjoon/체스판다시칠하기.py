from typing import List


def solution(N: int, M: int, board: List[str]) -> int:
    def get_dp(bw: str) -> List[List[int]]:
        dp = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                curr = 0
                # i-1기준으로 하면 안됨 i-1==0인경우도 포함
                if i > 0:
                    curr += dp[i - 1][j]
                if j > 0:
                    curr += dp[i][j - 1]
                if i > 0 and j > 0:
                    curr -= dp[i - 1][j - 1]
                # if not (i + j) & 1 and dp[i][j] == bw:
                #     curr += 1
                # elif (i + j) and dp[i][j] != bw:
                #     curr += 1
                # 다시 칠해야하는거니깐 맞지 않게 칠해진 경우 +=1하기
                if (i + j) % 2 and board[i][j] == bw:
                    curr += 1
                if (i + j) % 2 == 0 and board[i][j] != bw:
                    curr += 1
                # curr += (i + j) % 2 == 0 and board[i][j] == bw
                # curr += (i + j) % 2 != 0 and board[i][j] != bw
                dp[i][j] = curr
        return dp

    dp_b = get_dp("B")
    dp_w = get_dp("W")

    def get_colored_rectangle(i: int, j: int, bw: str) -> int:
        # inner function에서 outer function 변수 사용하기 위해 global 선언 필요 없음!
        # global은 함수 안에서 global variable 가져올 때 사용하는 것이기 때문
        dp = dp_b if bw == "B" else dp_w
        cnt = dp[i + 7][j + 7]
        # 여기 주의!
        if i > 0:
            cnt -= dp[i - 1][j + 7]
        if j > 0:
            cnt -= dp[i + 7][j - 1]
        if i > 0 and j > 0:
            cnt += dp[i - 1][j - 1]
        return cnt

    ans = 65

    for i in range(N - 7):
        for j in range(M - 7):
            ans = min(ans,
                      get_colored_rectangle(i, j, "B"),
                      get_colored_rectangle(i, j, "W"))

        return ans


# N, M = map(int, input().split())
# board = [input() for _ in range(N)]
N, M = 8, 8
board = ["WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBBBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW"]

print(solution(N, M, board))

N, M = 10, 13
board = ["BBBBBBBBWBWBW",
         "BBBBBBBBBWBWB",
         "BBBBBBBBWBWBW",
         "BBBBBBBBBWBWB",
         "BBBBBBBBWBWBW",
         "BBBBBBBBBWBWB",
         "BBBBBBBBWBWBW",
         "BBBBBBBBBWBWB",
         "WWWWWWWWWWBWB",
         "WWWWWWWWWWBWB"]

print(solution(N, M, board))
