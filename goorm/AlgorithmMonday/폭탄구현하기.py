from typing import List, Tuple


def get_affected_area_size(n: int, k: int, bomb: List[Tuple[int]]) -> int:
    area = [[0] * n for _ in range(n)]
    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    for row, col in bomb:
        area[row][col] += 1
        for k in range(4):
            new_row = row + dr[k]
            new_col = col + dc[k]
            if 0 <= new_row < n and 0 <= new_col < n:
                area[new_row][new_col] += 1

    return sum(square for row in area for square in row)


n, k = map(int, input().split())
bomb = []

for _ in range(k):
    row, col = map(lambda x: int(x) - 1, input().split())
    bomb.append((row, col))

print(get_affected_area_size(n, k, bomb))
