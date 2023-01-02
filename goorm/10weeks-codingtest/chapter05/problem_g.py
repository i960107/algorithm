from typing import List

'''숫자 채우기3'''


def solution(n: int) -> List[List[int]]:
    # 복잡도 O(N^2). N의 최대값 = 100.
    # O(N^2)보다 빠른 방법이 있을가? 예를 들어 수열을 이용해 값을 채우는 방법.
    EMPTY = -1
    arr = [[EMPTY] * n for _ in range(n)]
    return arr


def print_arr(n: int, arr: List[List[int]]):
    for i in range(n):
        print(*arr[i])


t = int(input())
for _ in range(t):
    n = int(input())
    res = solution(n)
    print_arr(n, res)
