from collections import deque
from typing import List


def solution_bfs_fail(N: int, M: int, arr: List[str]) -> int:
    '''bfs를  이용한 풀이'''
    dx = [1, 1, 0]
    dy = [0, 1, 1]

    def bfs(i, j) -> int:
        size = 1
        q = deque((i, j))
        while q:
            now_i, now_j = q.popleft()
            is_rectangle = True
            for k in range(3):
                if not arr[now_i + dy[k]][now_j + dx[k]]:
                    is_rectangle = False
            if is_rectangle:
                size += 1
        return 0

    max_rec = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                now = bfs(i, j)
                if now > max_rec:
                    max_rec = now
    return max_rec


def solution_dp(N: int, M: int, arr: List[str]) -> int:
    '''다이나믹 프로그래밍을 이용한 풀이'''
    dp = [[0] * M for _ in range(N)]
    max_rec_side = 0
    for i in range(1, N):
        for j in range(1, M):
            if not i or not j or dp[i][j] == "0":
                dp[i][j] = int(arr[i][j])
            elif arr[i][j] == "1":
                dp[i][j] = min(dp[i - 1][j],
                               dp[i - 1][j - 1],
                               dp[i][j - 1]) + 1
            max_rec_side = max(dp[i][j], max_rec_side)

    return max_rec_side ** 2


N, M = 4, 4
# arr = ["0100", "0111", "1110", "0010"]
arr = ["1111", "1111", "1111", "1111"]
print(solution_dp(N, M, arr))
