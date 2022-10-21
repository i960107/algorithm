from typing import List, Final
from collections import deque

'''토마토'''


class State:
    EMPTY: Final = -1
    RIPE: Final = 1
    UNRIPE: Final = 0

    def __init__(self, row: int, col: int, depth: int):
        self.row = row
        self.col = col
        self.depth = depth


def get_minimum_required_days(R: int, C: int, tomato: List[List[int]]) -> int:
    visited = [[False] * C for _ in range(R)]

    distance = [[0] * C for _ in range(R)]

    bfs_queue = deque()

    for row in range(R):
        for col in range(C):
            if tomato[row][col] == State.RIPE:
                bfs_queue.append(State(row, col, 1))

    while bfs_queue:
        current = bfs_queue.popleft()

        # 인덱스 체크
        if current.row < 0 or current.col < 0 or current.row >= R or current.col >= C:
            continue
        # 이미 방문한 곳 혹은 토마토가 없는 곳 제외
        elif visited[current.row][current.col]:
            continue

        if tomato[current.row][current.col] == State.EMPTY:
            continue

        visited[current.row][current.col] = True
        distance[current.row][current.col] = current.depth - 1

        bfs_queue.append(State(current.row + 1, current.col, current.depth + 1))
        bfs_queue.append(State(current.row - 1, current.col, current.depth + 1))
        bfs_queue.append(State(current.row, current.col + 1, current.depth + 1))
        bfs_queue.append(State(current.row, current.col - 1, current.depth + 1))

    unripe_count = 0
    required_days = 0
    for row in range(R):
        for col in range(C):
            if tomato[row][col] == State.EMPTY:
                continue
            if not visited[row][col]:
                unripe_count += 1
                break
            else:
                required_days = max(required_days, distance[row][col])

    return required_days if unripe_count == 0 else -1


C, R = map(int, input().split())

tomato = []
for _ in range(R):
    tomato.append(list(map(int, input().split())))

print(get_minimum_required_days(R, C, tomato))
