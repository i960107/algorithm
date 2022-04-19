from typing import List


def solution(tstring: str, variables: List[List[str]]) -> str:
    strings = []
    curr = ""
    for c in tstring:
        if c == "{":
            strings.append(curr)
            curr = c
        elif c == "}":
            curr += c
            strings.append(curr)
            curr = ""
        else:
            curr += c

    d = {}

    for variable, value in variables:
        d[variable] = value

    answer = ""

    def is_variable(s: str) -> bool:
        return s.startswith("{")


    # 상호참조


def is_cross_referenced(variable: str) -> bool:
    # variable에 해당하는 값이 변수가 아니라 단어일때
    if not is_variable(d[variable[1:-1]]):
        return False
    else:
        curr = d.get(variable[1:-1])
        while curr:

        if not d.get(variable2):
            return False
        else:
            return variable == d[d[variable[1:-1]][1:-1]]


for i, s in enumerate(strings):
    # if is_variable(s):
    #     value = d[s[1:-1]]
    #     # 값이 더이상 없거나, 상호 참조가 일어날때 혹은 더이상 변수가 아닐때 while문 종료
    #     while is_variable(value):
    #         # 현재 {}없어진 상태!
    #         if d.get(value[1:-1]) and not is_cross_referenced(value[1:-1]):
    #             value = d[value[1:-1]]
    #         # 값이 없을때는?
    #         else:
    #             break
    #     answer += value
    curr = s
    while is_variable(curr):
        if d.get(curr[1:-1]) and not is_cross_referenced(curr):
            curr = d[curr[1:-1]]
        else:
            break
    answer += curr
return answer

# ddd {d} {i} i는 값이 없고 d는 상호참조!
print(solution("{a} {b} {c} {d} {i}",
               [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]))
# print(solution("this is {template} {template} is {state}", [["template", "string"], ["state", "changed"]]))
# print(solution("this is {template} {template} is {state}", [["template", "string"], ["state", "{template}"]]))
# print(solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{templates}"]]))
# print(solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{template}"]]))
