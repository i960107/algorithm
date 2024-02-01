from typing import List


def solution(n: int, computers: List[List[int]]) -> int:
    def dfs(computer: int):
        print(computer, end=' ')
        visited[computer] = True
        for nxt in range(n):
            if visited[nxt] or not computers[computer][nxt]:
                continue
            dfs(nxt)

    # visited = [False * n] # 숫자의 곱셈
    visited = [False] * n  # 배열의 반복
    count = 0
    for i in range(n):
        if visited[i]:
            continue
        dfs(i)
        count += 1
        print()
    return count


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
