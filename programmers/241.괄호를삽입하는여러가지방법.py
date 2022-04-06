from typing import List


def solution(s: str) -> List[int]:
    # left와 right에는 항상 숫자 하나인 리스트만 들어옴?
    def compute(left: List[int], right: List[int], op):
        results = []
        for l in left:
            for r in right:
                print(f'{l} {op} {r}')
                results.append(eval(str(l) + op + str(r)))
        return results

    if s.isdigit():
        return [int(s)]

    results = []
    for index, value in enumerate(s):
        if value in "-+*":
            l = solution(s[:index])
            r = solution(s[index + 1:])
            results.extend(compute(l, r, value))

    return results


