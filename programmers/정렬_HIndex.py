def solution_wrong(citations: list) -> int:
    ''''틀린답 정확성 테스트 실패'''
    citations.sort(reverse=True)

    i = 0
    while i < len(citations) - 1:
        while citations[i] == citations[i + 1]:
            i += 1
        # h번이상 인용된 논문의 수 i+1개 >= h
        if citations[i] <= i + 1:
            return citations[i]
        else:
            i += 1
    return citations[-1]


def solution_others(citations: list) -> int:
    answer = 0
    citations.sort(reverse=True)

    for i, h in enumerate(citations):
        # 왜 i+1이 아닌 i? 왜 h가 아닌 i 리턴?
        if h <= i:
            return i
    else:
        return len(citations)


def solution_others2(citations: list) -> int:
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


print(solution_others2([3, 0, 6, 1, 5]))
# 만약 같은 값이 있을때 인용된 논문의 수..
print(solution_others2([1, 1, 1, 1, 0]))
