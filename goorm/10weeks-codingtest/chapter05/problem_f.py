from typing import List

'''숫자 채우기2'''


def test_case(case_index: int):
    n = int(input())

    EMPTY = -1
    arr = [[EMPTY] * n for _ in range(n)]

    delta_r = (0, 1, 0, 1, 0, -1)
    delta_c = (1, 0, -1, 0, 1, 0)

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


def test_case2(case_index: int):
    '''큰 숫자부터 내림차순으로 채우기'''
    # n에 따라서 방향 순서가 달라짐
    n = int(input())

    EMPTY = -1
    arr = [[EMPTY] * n for _ in range(n)]

    num = n * n
    if n % 2 == 0:
        r, c = n, 0
        delta_r = (0, -1, 0, 1, 0, -1)
        delta_c = (1, 0, -1, 0, -1, 0)
    else:
        r, c = 0, n
        delta_r = (1, 0, -1, 0, -1, 0)
        delta_c = (0, -1, 0, 1, 0, -1)
    direction = -1

    while True:
        nr, nc = r + delta_r[direction], c + delta_c[direction]
        # 방향 전환이 필요한 경우 1) 다음 칸의 인덱스가 범위를 벗어났을때 2) 다음 칸의 이미 채워진 칸일때 3) 현재 칸이 첫번째 행이거나 첫번째 열일때

        if not (0 <= nr < n and 0 <= nc < n) or arr[nr][nc] != EMPTY:
            direction = (direction + 1) % len(delta_r)
            continue

        arr[nr][nc] = num

        if num == 1:
            break

        r, c = nr, nc
        num -= 1

        if r == 0 or c == 0:
            direction = (direction + 1) % len(delta_r)

    print_arr(arr, n)


def test_case3(case_index: int):
    '''거듭 제곱수 이용하기'''
    # 어떻게 표현하는게 가장 좋은 방법일까?
    # n에 따라서 방향 순서가 달라짐
    n = int(input())

    EMPTY = -1
    arr = [[EMPTY] * n for _ in range(n)]

    # n과 상관없이 같은 위치에 같은 숫자가 위치!
    level = 0
    while True:
        if level % 2 == 0:
            num = level * level + 1
            r, c = level, 0
            arr[r][c] = num

            continue




    print_arr(arr, n)


def print_arr(arr: List[List[int]], n: int):
    for i in range(n):
        for j in range(n):
            print(str(arr[i][j]).ljust(3, " "), end="")
        print()


t = int(input())
for case_index in range(t):
    res = test_case2(case_index)
