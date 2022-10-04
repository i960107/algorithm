def solution(pos: str) -> int:
    dx = [-2, -2, 2, 2, -1, +1, -1, +1]
    dy = [-1, 1, 1, -1, 2, 2, -2, -2]

    # steps = ((-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2))

    x = ord(pos[0]) - 97
    y = int(pos[1]) - 1

    res = 0

    for k in range(8):
        nx = dx[k] + x
        ny = dy[k] + y

        if 0 <= nx < 8 and 0 <= ny < 8:
            res += 1

    return res


res = solution("a1")
print(res, res == 2)
