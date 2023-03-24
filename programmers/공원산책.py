from typing import List


def solution(park: List[str], routes: List[str]) -> List[int]:
    directions = {
        "E": (0, 1),
        "W": (0, -1),
        "S": (1, 0),
        "N": (-1, 0)
    }
    OBSTACLE = "X"
    START = "S"

    R = len(park)
    C = len(park[0])

    sr = sc = None
    for r in range(R):
        for c in range(C):
            if park[r][c] == START:
                sr, sc = r, c
                break

    r, c = sr, sc
    for route in routes:
        print(r, c)
        direction, count = route.split()
        # 원래 좌표를 기억해야 함.
        now_r, now_c = r, c
        for _ in range(int(count)):
            nxt_r, nxt_c = now_r + directions[direction][0], now_c + directions[direction][1]
            if not (0 <= nxt_r < R and 0 <= nxt_c < C) or park[nxt_r][nxt_c] == OBSTACLE:
                now_r, now_c = r, c
                break
            now_r, now_c = nxt_r, nxt_c
        r, c = now_r, now_c

    return [r, c]


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
