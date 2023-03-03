from typing import List
from sys import stdin


def find_root(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]


def union(parent: List[int], a: int, b: int):
    a = find_root(parent, a)
    b = find_root(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


read = stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    op, a, b = map(int, read().split())
    if op == 0:
        union(parent, a, b)
    else:
        a = find_root(parent, a)
        b = find_root(parent, b)
        print("YES" if a == b else "NO")
