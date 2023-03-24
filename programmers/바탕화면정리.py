from typing import List


def solution(wallpaper: List[str]) -> List[int]:
    X, Y = len(wallpaper), len(wallpaper[0])
    lux = X
    luy = Y
    rdx = 0
    rdy = 0

    for x in range(X):
        for y in range(Y):
            if wallpaper[x][y] == ".":
                continue
            if x < lux:
                lux = x
            if x > rdx:
                rdx = x
            if y < luy:
                luy = y
            if y > rdy:
                rdy = y

    rdx += 1
    rdy += 1
    return [lux, luy, rdx, rdy]


print(solution([".#...", "..#..", "...#."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))
