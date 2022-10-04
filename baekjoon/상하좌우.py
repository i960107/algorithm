from typing import List


def solution(N: int, path: List[str]) -> List[int]:
    x, y = 0, 0

    for move in path:
        if move == "L":
            cx, cy = x - 1, y
        elif move == "R":
            cx, cy = x + 1, y
        elif move == "U":
            cx, cy = x, y - 1
        else:
            cx, cy = x, y + 1

        if not (0 <= cx < N) or not (0 <= cy < N):
            continue
        x, y = cx, cy
    return [y + 1, x + 1]


res = solution(5, ["R", "R", "R", "U", "D", "D"])
print(res == [3, 4])
