import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
inf = float('inf')

n = int(input())
cache = [inf] * (n + 1)
cache[1] = 0


def solution_dp(x):
    if cache[x] != inf:
        return cache[x]

    if x % 6 == 0:
        # list indices must be integer
        cache[x] = min(solution_dp(x // 2), solution_dp(x // 3)) + 1
    elif x % 3 == 0:
        cache[x] = min(solution_dp(x // 3), solution_dp(x - 1)) + 1
    elif x % 2 == 0:
        cache[x] = min(solution_dp(x // 2), solution_dp(x - 1)) + 1
    else:
        cache[x] = solution_dp(x - 1) + 1

    return cache[x]


print(solution_dp(n))


def solution_bfs(x):
    dq = deque([(x, 0)])

    # 최초로 한번 도달한 곳은 이후에 다시 도달할 필요 없음(더 긴 경로임). 가지치기
    chk = [False] * (x + 1)
    chk[x] = True
    while dq:
        # 매번 count해주면 안됨 (curr, count)를 튜플로 넣어줘야함
        # num < 1 인 경우는 없음
        num, dist = dq.popleft()
        if num == 1:
            return dist
        if num % 3 == 0 and not chk[num // 3]:
            chk[num // 3] = True
            dq.append((num // 3, dist + 1))
        if num % 2 == 0 and not chk[num // 2]:
            chk[num // 2] = True
            dq.append((num // 2, dist + 1))
        if not chk[num - 1]:
            chk[num - 1] = True
            dq.append((num - 1, dist + 1))


print(solution_bfs(n))
