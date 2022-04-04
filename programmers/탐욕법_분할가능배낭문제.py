from typing import List, Tuple


def solution(cargo: List[Tuple[int, int]], weight: int) -> float:
    answer = 0
    cargo = sorted(cargo, key=lambda x: x[0] / x[1])

    while weight > 0:
        if cargo[-1][1] <= weight:
            bag = cargo.pop()
            answer += bag[0]
            weight -= bag[1]
        else:
            bag = cargo.pop()
            answer += bag[0] / bag[1] * weight
            weight -= weight

    return answer


print(solution([(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)], 15))
