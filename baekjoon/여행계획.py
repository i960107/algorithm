from typing import List


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


N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

parent = [i for i in range(N + 1)]
for a in range(N):
    for b in range(N):
        if grid[a][b] == 1:
            union(parent, a + 1, b + 1)

possible = True
group_id = -1

places = list(map(int, input().split()))
for place in places:
    if group_id == - 1:
        group_id = find_root(parent, place)
        continue
    if find_root(parent, place) != group_id:
        possible = False
        break

print(parent)
print("YES" if possible else "NO")
