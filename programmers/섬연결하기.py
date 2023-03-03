from typing import List


def find(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: List[int], a: int, b: int):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n: int, costs: List[List[int]]) -> int:
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    total_cost = 0
    for a, b, cost in costs:
        a = find(parent, a)
        b = find(parent, b)

        if a == b:
            continue
        union(parent, a, b)
        total_cost += cost
    return total_cost


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
