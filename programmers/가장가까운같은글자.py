from typing import List


def solution(s: str) -> List[int]:
    answer = []
    d = dict()
    for index, chr in enumerate(s):
        if chr not in d:
            answer.append(-1)
        else:
            answer.append(index - d[chr])
        d[chr] = index
    return answer


print(solution("banana"))
