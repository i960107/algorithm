from collections import deque

adj = [[]]  # 입력 받은 그래프. 사방으로 연결된 형태. 격자칸 형태의 board.
ans = 0  # 찾는 값

# y 행 x 열을 나타냄
# 위 오른쪽 아래 왼쪽을 나타냄
dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

N = int(input())
chk = [[False] * N for _ in range(N)]


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


def dfs(y, x):
    if adj[y][x] == ans:
        return
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        # 인덱스가 유효하고 아직 방문하지 않은 곳이라면
        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            chk[ny][nx] = True
            dfs(ny, nx)


def bfs(sy, sx):
    q = deque()
    chk[sy][sx] = True
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        if adj[y][x] == ans:
            return
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx))
