from collections import deque
from typing import List


def solution(N: int, M: int, maze: List[str]) -> int:
    # [n-1, m-1]에 도착하는 최소 경로
    # 전형적인 길찾기 문제. 시작노드 목표노드가 고정되어있고 갈 수 있는 칸과 없는 칸이 있다.
    # 최단거리를 구하기 위해 BFS를 쓰기
    # 왜 y가 행을 나타내로 x가 열을 나타낼까? 좌표평면으로 볼 수 도 있게!
    # 행이 y 열이 x로 보는 연습
    # 위, 오른쪽, 아래, 왼쪽
    # 오른쪽, 아래로만 이동할 수 있는 것 아님
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    dq = deque()
    # 행, 열, (0,0)부터 지나야하는 최소 칸의 수. 지나온 거리
    # BFS는 큐로 구현
    dq.append((0, 0, 1))
    # 방문 체크를 하지 않으면 이미 지나온 곳을 다시 방문하게 되어 큐가 계속 쌓여 메모리가 과도하게 사용되고. 무한반복
    chk = [[False] * M for _ in range(N)]

    def is_valid_coord(ny: int, nx: int) -> bool:
        return 0 <= ny < N and 0 <= nx < M

    while dq:
        y, x, d = dq.popleft()

        if y == N - 1 and x == M - 1:
            return d

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nd = d + 1
            # 갈수 있는 길이고 아직 탐색하지 않은 곳이라면
            # chk 이미 탐색한 곳이라면? -> 최단 거리보다 긴 경로라는 뜻. BFS이기 때문에
            if is_valid_coord(ny, nx) and maze[ny][nx] == "1" and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))


N, M = map(int, input().split())
maze = []
for _ in range(N):
    # 리스트로 바꿔줘도되고 그냥 string으로 써도 됨
    # maze.append(list(map(int, list(input()))))
    maze.append(input())

print(solution(N, M, maze))
