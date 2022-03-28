def solution_get_Jaden_Case(s: str) -> str:
    answer = ""
    # for문보다 while이 나을듯.
    # 공백 문자 만났을때 공백 다음의 문자 변경필요. 공백 다음의 문자를 다시 변경하면 안됨
    i = 0
    while i < len(s):
        # 앞에 문자와 비교하기 vs 뒷 문자와 비교하기
        # 앞에 문자가 공백이거나 없는데 현재 문자가 알파벳이면 upper case. 나머지 lower
        # 현재 문자가 공백이거나 첫번째인데 뒷문자가 알파벳이면

        curr = s[i]
        # 가장 앞문자이거나 앞에 문자가 공백일때
        if curr.isalpha():
            # 공백 문자열은 빈 문자열 아님!!!!!
            if i == 0 or (i > 0 and s[i - 1] == ' '):
                curr = curr.upper()
            else:
                curr = curr.lower()

        answer += curr
        i += 1

    return answer


print(solution_get_Jaden_Case("3people unFollowed me"))
print(solution_get_Jaden_Case("for the last week"))
print(solution_get_Jaden_Case(" 12345 "))
