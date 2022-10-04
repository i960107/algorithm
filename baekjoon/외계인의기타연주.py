from typing import List


def solution(N: int, P: int, melody: List[List[int]]):
    stk = [[] for _ in range(6)]
    cnt = 0
    for l, p in melody:
        if not stk[l - 1] or stk[l - 1][-1] < p:
            cnt += 1
            stk[l - 1].append(p)
        elif stk[l - 1][-1] > p:
            while stk[l - 1] and stk[l - 1][-1] > p:
                cnt += 1
                stk[l - 1].pop()

            if not stk[l - 1] or stk[l - 1][-1] != p:
                cnt += 1
                stk[l - 1].append(p)
    return cnt


N, P = 5, 15
melody = [[2, 8], [2, 10], [2, 12], [2, 10], [2, 5]]
print(solution(N, P, melody))
