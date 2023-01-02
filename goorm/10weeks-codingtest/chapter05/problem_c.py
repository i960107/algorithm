from typing import List,Tuple

'''레이저 타워'''


def solution(n: int, k: int, grid: List[List[int]], candidate: List[Tuple[int]]) -> int:
    #예외) 이미 특수시설이 존재하는 칸에 레이저 타워를 건설할 수 있다!
    answer = 0
    return answer


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    candidates = []
    for _ in range(k):
        r, c = map(int, input().split())
        candidates.append((r, c))
    res = solution(n, k, grid, candidates)
    print(res)

