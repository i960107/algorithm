from collections import Counter


# 문제 제대로 읽기! 얘시 꼼꼼히 살피기
def solution_fail(X: str, Y: str) -> str:
    # 어떻게 하는게 가장 좋을까? 사실 똑같음..
    pair = []
    length = min(len(X), len(Y))
    for x, y in zip(X[-length:], Y[-length:]):
        if x == y:
            pair.append(x)
    if not pair:
        return "-1"
    pair.sort(reverse=True)

    return ''.join(pair)


def solution(X: str, Y: str) -> str:
    x_counter = Counter(X)
    y_counter = Counter(Y)

    numbers = []
    for x, count in x_counter.items():
        if x not in y_counter:
            continue
        for _ in range(min(count, y_counter[x])):
            numbers.append(x)

    # 공통된 숫자가 없는 경우
    if not numbers:
        return "-1"

    # 공통된 숫자가 0뿐인 경우
    numbers.sort(reverse=True)
    if numbers[0] == "0":
        return "0"

    return ''.join(numbers)


print(solution("100", "2345"))
print(solution("100", "203045"))
