from typing import List
from collections import deque


def solution(n, m, arr: List[List[int]]) -> int:
    di = (-1, 1, 0, 0)
    dj = (0, 0, -1, 1)

    def is_sunk(i: int, j: int) -> bool:
        return arr[i][j] == 0

    def get_affected_area() -> List[List[int]]:
        affected = []
        for i in range(n):
            for j in range(m):
                if not is_sunk(i, j):
                    continue
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < n and 0 <= nj < m and not is_sunk(ni, nj):
                        affected.append([ni, nj])
        return affected

    def update_sank_area():
        for i, j in get_affected_area():
            arr[i][j] = 0

    def bfs(i, j, visited):
        # if i < 0 or i >= n or j < 0 or j >= m:
        #     return
        # if is_sunk(i, j):
        #     return
        # if visited[i][j]:
        #     return
        # visited[i][j] = True
        # for k in range(4):
        #     ni, nj = i + di[k], j + dj[k]
        #     bfs(ni, nj, visited)
        queue = deque()
        queue.append((i, j))
        while queue:
            ci, cj = queue.popleft()
            if ci < 0 or ci >= n or cj < 0 or cj >= m:
                continue
            if is_sunk(ci, cj):
                continue
            if visited[ci][cj]:
                continue
            visited[ci][cj] = True
            for k in range(4):
                ni, nj = ci + di[k], cj + dj[k]
                queue.append((ni, nj))
        return visited

    def get_island_count() -> int:
        visited = [[False] * m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                if is_sunk(i, j):
                    continue
                count += 1
                bfs(i, j, visited)
        return count

    day = 0
    islands = get_island_count()
    while islands < 2:
        day += 1
        update_sank_area()
        islands = get_island_count()
        if islands == 0:
            return -1

    return day


n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
print(solution(n, m, arr))
