from typing import List, Tuple


# dfs  -> 사이클 있는지 판별. dfs에서 시작노드를 만나면.
# visited하면 안되지 않나... 방은 다른 방으로 둘러싸여질 수 있기 때문에.
# 2차원 행렬의 union-find 어떻게...?
def solution(arrows: List[int]) -> int:
    def find(r: int, c: int) -> Tuple[int, int]:
        if parent[r][c] != (r, c):
            # 튜플은 값으로 비교되나, id로 비교되나?
            parent[r][c] = find(*parent[r][c])
        return parent[r][c]

    def union(r1: int, c1: int, r2: int, c2: int):
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)

        # 더 작은 수를 가리키도록
        if r1 < r2 or (r1 == r2 and c1 < c2):
            parent[r2][c2] = (r1, c1)
        else:
            parent[r1][c1] = (r2, c2)

    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    min_r = min_c = 100000
    max_r = max_c = 0
    r, c = 0, 0
    for arrow in arrows:
        r += direction[arrow][0]
        c += direction[arrow][1]
        if r < min_r:
            min_r = r
        if c < min_c:
            min_c = c
        if r > max_r:
            max_r = r
        if c > max_c:
            max_c = c

    R = max_r - min_r + 1
    C = max_c - min_c + 1

    # 첫 시작 포인트를 어떻게 잡지..
    graph = [[r * C + c for c in range(C)] for r in range(R)]
    # 2차원 행렬의 Union find를 위해서는 부모를 뭘로 초기호ㅑ?
    parent = [[(r, c) for c in range(C)] for r in range(R)]

    r, c = - min_r, - min_c
    rooms = 0
    for arrow in arrows:
        nr = r + direction[arrow][0]
        nc = c + direction[arrow][1]
        if find(r, c) == find(nr, nc):
            rooms += 1
        union(r, c, nr, nc)
        r, c = nr, nc
    return rooms


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
# 인스턴스 id가 아닌 값이 비교됨
# print((1, 2) == (1, 2))
# print([1, 2] == [1, 2])
