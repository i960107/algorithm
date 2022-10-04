from typing import List


def solution(N: int, M: int, board: List[str]) -> int:
    k = 0

    while k < 10:
        pass

    return -1


res = solution(5, 5, ["#####", "#..B#", "#.#.#", "#RO.#", "#####"])
print(res, res == 1)

res = solution(7, 7, ["#######", "#...RB#", "#.#####", "#.....#", "#####.#", "#######"])
print(res, res == 5)
