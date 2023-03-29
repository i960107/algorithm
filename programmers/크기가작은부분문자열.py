from datetime import datetime as d


def solution(t: str, p: str) -> int:
    P = len(p)
    p = int(p)
    count = 0
    for start in range(len(t) - P + 1):
        part_t = int(t[start: start + P])
        if part_t <= p:
            count += 1
    return count


def solution2(t: str, p: str) -> int:
    count = 0

    if len(p) == 1:
        # 한글자인경우 사전순으로 비교해도 됨
        return sum([1 for x in t if x <= p])

    for start in range(len(t) - len(p) + 1):
        is_greater = False
        # 한자리인 경우 어떻게 처리되어야하는지 주의 -> 그대로
        # 같을때 어떻게 처리되어야하는지 주의
        # 같은 수인 경우 is_greater = False인 채로 빠져나옴
        for index, digit in enumerate(p):
            if t[start + index] < digit:
                break

            if t[start + index] > digit:
                is_greater = True
                break

        if not is_greater:
            count += 1

    return count


print(solution2("3141592", "271"))
print(solution2("50022083978", "7"))
print(solution2("10203", "15"))
