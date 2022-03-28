def solution(s: str) -> int:
    result = []

    # 빈 문자열, 문자1인경우 주의!!
    if len(s) <= 1:
        return len(s)

    # 문자열의 절반까지 자를 수 있는지 탐색?
    # 문자열은 제일 앞부터 정해진 길이만큼 잘라야함!
    # 모든 문자에 대해 같을 길이로 압축! 2문자 압축후 1문자 압축 아님!!
    for i in range(1, len(s) // 2 + 1):
        comp = ''
        cnt = 1
        tmp = s[:i]
        # 같은 문자 찾을때까지?
        for j in range(i, len(s), i):
            curr = s[j:j + i]
            if curr == tmp:
                cnt += 1
            else:
                if cnt != 1:
                    comp = comp + str(cnt) + tmp
                else:
                    comp = comp + tmp
                tmp = curr
                cnt = 1

        if cnt != 1:
            comp = comp + str(cnt) + tmp
        else:
            comp = comp + tmp

        result.append(len(comp))

    # O(2N)?
    return min(result)


print(solution("aabbacc"))
print(solution("a"))
print(solution(""))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
