from collections import deque


def solution(storey: int) -> int:
    # 0층에서 storey까지 가는 최단거리
    count = 0
    floor = storey
    while floor != 0:
        c = 0
        move = floor // (10 ** c)
        while move >= 10:
            c += 1
            move = move // 10
        floor -= (10 ** c) * move
        count += move

    return count


print(solution(2554))
print(solution(16))

