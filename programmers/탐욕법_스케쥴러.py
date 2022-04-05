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


def solution_others(tasks: List[str], n: int) -> int:
    counter = Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        # 개수 순 추출
        # most_common()은 가장 개수가 많은 아이템을 출력하는 함수로 사실상 최대 힙과 같은 역할ㅇ르 한다
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0이하인 아이템을 목록에서 완전히 제거
            # 빈 컬렉션을 더하면 0 이하인 아이템을 목록에서 제거해버리는 핵
            counter += Counter()
        if not counter:
            break
        result += n - sub_count + 1

    return result


print(solution_others(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(solution_others(tasks=["A", "A", "A", "B", "B", "B"], n=0))
print(solution_others(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
