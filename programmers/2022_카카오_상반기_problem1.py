from typing import List


def solution(survey: List[str], choices: List[int]) -> str:
    # 각 성격 유형 별로 8개 별 점수 계산?
    # -> 성격 유형별로 연결짓는 해시하나, 성격 유형별 점수 계산하는 배열 필요
    # 정렬한 결과로 점수 계산 4개로?
    # -> 매변 정렬하는거 너무 비효율적인가?
    types = {
        "RT": 0,
        "CF": 0,
        "JM": 0,
        "AN": 0
    }

    for type, choice in zip(survey, choices):
        sorted_type = "".join(sorted(type))
        if type == sorted_type:
            types[type] += (choice - 4)
        else:
            types[sorted_type] -= (choice - 4)

    print(types)

    return "".join(type[score > 0] for type, score in types.items())


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))


def solution2(survey: List[str], choices: List[int]) -> str:
    types = {
        "R" : "T",
        "T": "R",
        "C": "F",
        "F": "C",
        "J": "M",
        "M": "J",
        "A": "N",
        "N": "A",
    }
    scores =

    for type, choice in zip(survey, choices):
        if choice > 4:
            R.index(type[1])


print(solution2(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution2(["TR", "RT", "TR"], [7, 1, 3]))
