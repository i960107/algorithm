from typing import List


def solution(N: int, L: int, holes: List[int]) -> int:
    tape = 0
    x = 0
    for hole in holes:
        if x < hole:
            tape +=1
            x = hole + L -1
    return tape


N, L = map(int, input().split())
holes = list(map(int, input().split()))
print(solution(N, L, holes))
