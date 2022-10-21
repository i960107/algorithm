from typing import List
from collections import deque

''''미로 탈출하기'''


class State:
    def __init__(self, row: int, col: int, depth: int):
        self.row = row
        self.col = col
        self.depth = depth


def get_shortest_path_length(R: int, C: int, origin_r: int, origin_c: int, dest_r: int, dest_c: int,
                             passable: List[str]) -> int:
    bfs_queue = deque()
    bfs_queue.append(State(origin_r, origin_c, 1))

    # 가장 자리에 dummy 헤드를 추가해서 원소들이 1 ~ R, 1 ~ C의 값을 가지도록
    visited = [[False] * (C + 2) for _ in range(R + 2)]
    distance = [[0] * (C + 2) for _ in range(R + 2)]

    while bfs_queue:
        current = bfs_queue.popleft()

        if current.row < 1 or current.col < 1 or current.row > R or current.col > C:
            continue

        if visited[current.row][current.col] or not passable[current.row][current.col]:
            continue

        visited[current.row][current.col] = True
        distance[current.row][current.col] = current.depth - 1

        bfs_queue.append(State(current.row + 1, current.col, current.depth + 1))
        bfs_queue.append(State(current.row - 1, current.col, current.depth + 1))
        bfs_queue.append(State(current.row, current.col + 1, current.depth + 1))
        bfs_queue.append(State(current.row, current.col - 1, current.depth + 1))

    if not visited[dest_r][dest_c]:
        return -1

    return distance[dest_r][dest_c]


R, C = map(int, input().split())
passable = [[False] * (C + 2) for _ in range(R + 2)]
origin_r, origin_c, dest_r, dest_c = -1, -1, -1, -1

for row in range(1, R + 1):
    line = list(input())
    for col in range(1, C + 1):
        c = line[col - 1]
        if c != "#":
            passable[row][col] = True
        if c == "S":
            origin_r, origin_c = row, col
        elif c == "E":
            dest_r, dest_c = row, col

print(get_shortest_path_length(R, C, origin_r, origin_c, dest_r, dest_c, passable))
