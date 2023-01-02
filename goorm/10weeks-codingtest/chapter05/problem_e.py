from typing import List

'''숫자 채우기1'''


def test_case(case_index: int) -> List[List[int]]:
    n = int(input())

    EMPTY = -1
    arr = [[EMPTY] * n for _ in range(n)]

    delta_r = (0, 1, 0, -1)
    delta_c = (1, 0, -1, 0)

    direction = 0
    r, c = 0, -1

    index = 0
    last_index = n * n

    while True:
        if index == last_index:
            break

        nr, nc = r + delta_r[direction], c + delta_c[direction]

        if not (0 <= nr < n and 0 <= nc < n) or arr[nr][nc] != EMPTY:
            direction = (direction + 1) % len(delta_c)
            continue

        index += 1

        arr[nr][nc] = index
        r, c = nr, nc

    print_arr(arr, n)
    return arr


def print_arr(arr: List[List[int]], n: int):
    for i in range(n):
        print(*arr[i])


t = int(input())
for case_index in range(t):
    res = test_case(case_index)
