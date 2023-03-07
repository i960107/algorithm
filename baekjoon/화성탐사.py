from typing import List
from collections import defaultdict
import heapq


# 플로이드 워셜인줄 알앗는데 아니네...
# grid[i][j]가 i에서 j로 가는 비용이 아니라 그 칸에서 다른 칸으로 가는 비용임
def dp(N: int, grid: List[List[int]]) -> int:
    # (1, 1) (1, 2) (2,2) (2,1)로 가는게 더 나은 경우는 없나?
    # 각 칸의 비용은 양수기이때문에 더 많은 칸을 지날수록 더 비용이 커짐
    for i in range(N):
        for j in range(N):
            cost = int(1e9)
            if i == j == 0:
                continue
            if i - 1 >= 0:
                cost = min(cost, grid[i - 1][j])
            if j - 1 >= 0:
                cost = min(cost, grid[i][j - 1])
            grid[i][j] += cost
    for row in grid:
        print(row)
    return grid[N - 1][N - 1]


def dijkstra(N: int, grid: List[List[int]]) -> int:
    INF = int(1e9)

    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    costs = [[INF] * N for _ in range(N)]
    queue = []
    queue.append((grid[0][0], 0, 0))

    while queue:
        acc_cost, r, c = heapq.heappop(queue)

        if costs[r][c] < acc_cost:
            continue

        costs[r][c] = acc_cost

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            next_cost = acc_cost + grid[nr][nc]
            if costs[nr][nc] < next_cost:
                continue
            costs[nr][nc] = next_cost
            heapq.heappush(queue, (next_cost, nr, nc))

    return costs[N - 1][N - 1]


def solution(n: int, graph: List[List[int]]) -> int:
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    distance = [[int(1e9)] * n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]  # 비용, x, y
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))
    return distance[n - 1][n - 1]


T = int(input())
for _ in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    print(dijkstra(N, grid))
