from typing import List
from collections import deque


class Sail:
    # direction 1: 우측
    # direction 2: 우측 아래
    # direction 3: 아래
    # direction 4: 좌측 아래
    # direction 5: 좌측
    # direction 6: 좌측 위
    # direction 7: 위
    # direction 8: 우측 위

    def __init__(self, i: int, j: int, direction: int, level: int):
        self.i = i
        self.j = j
        self.direction = direction
        self.level = level

    def rotate_right_and_move(self) -> List[int]:
        pass

    def move_straight(self) -> List[int]:
        pass


def solution(worldmap: List[str]) -> int:
    def can_rotate_left(current: Sail) -> bool:
        can_rotate_left = True

        if current.direction in (1, 2):
            if worldmap[current.i-1][current.j - 1] == "X":
                return False
            if current.direction == 1:
                worldmap[current.i][current.j]

        elif current.direction == (3, 4):
            if worldmap[current.i][current.j + 1] == "X":
                return False
        elif current.direction == (5, 6):
            if worldmap[current.i +1][current.j] == "X":
                return False
        elif current.direction == (7, 8):
            if worldmap[current.i ][current.j- 1] == "X":
                return False

        if worldmap[left_i][left_j] == "X":
            can_rotate_left = False

        if current.direction in (1, 3, 5, 7):
            if worldmap[current.i - 1][current.j] == "X" or worldmap[current.i][current.j - 1] == "X":

        return can_rotate_left

    def rotate_left_and_move(current: Sail) -> Sail:
        pass

    n, m = len(worldmap), len(worldmap[0])
    i, j = 0, 0
    target_i, target_j = n - 1, m - 1
    bfs_queue = deque()
    bfs_queue.append(Sail(i, j, 1, 0))

    while bfs_queue:
        current = bfs_queue.popleft()
        left_sail = current.rotate_left_and_move()
        right_sail = current.rotate_right_and_move()
        straight_sail = current.move_straight()


print(solution(["..XXX", "..XXX", "...XX", "X....", "XXX.."]))
