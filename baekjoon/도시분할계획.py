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
roads = []
for _ in range(M):
    a, b, cost = map(int, read().split())
    roads.append((cost, a, b))
roads.sort()

costs = []
parent = [i for i in range(N + 1)]
for cost, a, b in roads:
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a == b:
        continue
    union(parent, a, b)
    costs.append(cost)

costs.pop()
print(sum(costs))
