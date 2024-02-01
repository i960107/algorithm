from typing import List
from collections import deque


def solution(nums: List[List[int]]) -> int:
    WALL, PASS = 0, 1
    rows, cols = len(nums), len(nums[0])
    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    queue = deque()
    # 이미 방문한 곳 방문하지 않도록.
    nums[0][0] = WALL
    queue.append((0, 0, 1))

    # 최단 거리
    answer = -1
    while queue:
        r, c, step = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            answer = step
            break
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if nums[nr][nc] == WALL:
                continue
            nums[nr][nc] = WALL
            queue.append((nr, nc, step + 1))
    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
