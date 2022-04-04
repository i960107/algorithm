from typing import List
from collections import Counter


def solution(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)

    unit = 0
    counter = Counter(tasks)

    if len(counter) <= 1:
        unit = len(counter) + (len(counter) - 1) * n

    elif len(counter) == 2:

        # 콤비로 진행되는 것
        combi_cnt = min(counter.values())
        for key, value in counter.items():
            counter[key] -= combi_cnt
        unit += combi_cnt * 2 + (combi_cnt - 1) * n

        residual = sum(counter.values())
        unit += residual + (residual - 1) * n

    return unit


print(solution(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(solution(tasks=["A", "A", "A", "B", "B", "B"], n=0))
print(solution(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
