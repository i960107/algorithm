from typing import List


def solution(N: int, M: int, pos: List[int], area: List[List[int]]) -> int:
    direction = (3, 0, 1, 2)

    dx = (-1, 0, 1, 0)
    dy = (0, -1, 0, 1)

    bx = (0, -1, 0, 1)
    by = (1, 0, -1, 0)

    # 현재좌표 방문처
    answer = 1

    while True:
        cx, cy, cd = pos

        print("현재", cx, cy, cd)

        found = False

        for k in range(4):
            nx, ny, nd = cx + dx[(cd + k) % 4], cy + dy[(cd + k) % 4], direction[(cd + k) % 4]
            print("nx", nx, ny, nd)

            if not (0 <= ny < M) or not (0 <= nx < N) or area[ny][nx] == 1:
                pos[2] = nd

            else:
                pos[0] = nx
                pos[1] = ny
                pos[2] = nd
                area[ny][nx] = 1
                answer += 1
                found = True
                break

        if not found:
            # 바라보는 방향을 유지한채 한칸 뒤로
            nx = pos[0] + bx[pos[2]]
            ny = pos[1] + by[pos[2]]
            if area[ny][nx] == 0:
                answer += 1
                area[ny][nx] = 1
                pos[0] = nx
                pos[1] = ny
            else:
                break

    return answer


def solution2(N: int, M: int, pos: List[int], area: List[List[int]]) -> int:
    x, y, direction = pos
    answer = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def turn_left():
        global direction
        direction = (direction - 1) % 4

    while True:
        for k in range(4):
            turn_left()

    return answer


res = solution(4, 4, [1, 1, 0], [[1, 1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]])
print(res, res == 3)
