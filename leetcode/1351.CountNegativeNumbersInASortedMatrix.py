from typing import List


def countNegatives(grid: List[List[int]]) -> int:
    r, n = len(grid), len(grid[0])
    c, count = 0, 0
    while r > 0 and c < n:
        if grid[r - 1][c] < 0:
            count += n - c
            r -= 1
        else:
            c += 1
    return count
