from collections import deque
from typing import List


def solution(R: int, C: int, board: List[str]) -> int:
    '''BFS 방식 백트래킹'''
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    # 지금까지 지나온 모든 칸에 적혀있는 알파벳 어떻게 기록하지 path? 여러가지 일 수 있는데
    def is_valid_coord(y, x):
        return 0 <= y < R and 0 <= x < C

    # 좌표와 그때까지 지나온 알파벳들을 연결한 문자열 -> 각 칸까지 지나온 알파벳이 동일하면 또 탐색하지 않아도됨
    # 다음에 다 시 이 칸을 방문할때 지나온 알파벳 문자열이 이미 집합에 있다면 탐색을 더 진행하지 않고 가지치기.
    dq = deque()
    # 지나온 경로 문자열을 set으로 관리
    # dq에 저장하는 경로 문자열과 어떻게 다른가? 직접 지나가고 있는 경로 dq에 저장. 거기까지 도달할 수 있는 모든 경로 chk에 저장.
    chk = [[set() for _ in range(C)] for _ in range(R)]
    ans = 0

    chk[0][0].add(board[0][0])
    dq.append((0, 0, board[0][0]))

    while dq:
        y, x, s = dq.popleft()
        ans = max(ans, len(s))

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] not in s:
                ns = s + board[ny][nx]
                if ns not in chk[ny][nx]:
                    chk[ny][nx].add(ns)
                    dq.append((ny, nx, ns))

    return ans


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input())

print(solution(R, C, board))
