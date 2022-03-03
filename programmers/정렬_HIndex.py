def solution_wrong(citations: list) -> int:
    ''''틀린답 정확성 테스트 실패'''
    citations.sort(reverse=True)

    # i = 0
    # while i < len(citations) - 1:
    #     while citations[i] == citations[i + 1]:
    #         i += 1
    #     # h번이상 인용된 논문의 수 i+1개 >= h
    #     if citations[i] <= i + 1:
    #         return citations[i]
    #     else:
    #         i += 1
    for i, h in enumerate(citations):
        if i + 1 >= h:
            return h


def solution_others(citations: list) -> int:
    answer = 0
    citations.sort(reverse=True)

    # for i, h in enumerate(citations):
    #     # 왜 i+1이 아닌 i? 왜 h가 아닌 i 리턴?i는 h랑 같을수도 다를 수도. 이때 몇편의 논문이 해당하는지 아닌 몇 회 기준인지를 반환하는 것!
    #     # h번이상 이용된 논문의 수 i+1이 h편이상이면
    #     # h번 인용된 논문의 수가 여러개일때,
    #     if h <= i:
    #         return i
    # else:
    #     return len(citations)
    # citations안 원소의 값만 h가 될 수 있는 것 아님! 0 <=h <= len(ciations)
    for i in range(len(citations)):
        # 여기가 뭔지 모르겠어
        # 이번 값에 해당하는 citations[i]보다 크거가 같은 값의 개수는 최소 i개
        if citations[i] <= i:
            return i
    # 인용 횟수가 모두 논문의 수를 초과할때!
    return len(citations)


def solution_others2(citations: list) -> int:
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


# print(solution_others([3, 0, 6, 1, 5]))
# # # h와 h번이상 인용된 논문의 수의 개수가 다를때.
# print(solution_others([2, 0, 6, 1, 5]))
# # 만약 같은 값이 있을때 인용된 논문의 수..
# 2번이상 인용된 논문의 수 2 h =1 아니라 2임.
print(solution_others([3, 3, 0, 1, 1, 1, 1, 1]))
# print(solution_others([1, 1, 1, 1, 0]))
# print(solution_others([10, 10, 10, 10, 10]))
# print(solution_others([0, 0, 0, 0, 0]))

# print(solution_others2([3, 0, 6, 1, 5]))
# # h와 h번이상 인용된 논문의 수의 개수가 다를때.
# print(solution_others2([2, 0, 6, 1, 5]))
# # 만약 같은 값이 있을때 인용된 논문의 수..
# print(solution_others2([3, 3, 0, 1, 1, 1, 1, 1]))
# print(solution_others2([1, 1, 1, 1, 0]))
# # len(ciations)출력되는 경우
# print(solution_others2([10, 10, 10, 10, 10]))
# print(solution_others2([0, 0, 0, 0, 0]))
# # h : h번이상 인용된 논문의 수
