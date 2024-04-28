def solution(s: str) -> int:
    n = 3
    candidates = []
    temp = ""
    count = 0
    for i in range(len(s)):
        if temp != s[i]:
            temp = s[i]
            count = 1
        elif temp == s[i]:
            count += 1
        if count == 3:
            candidates.append(temp)
    if len(candidates) == 0:
        return - 1
    candidates.sort(reverse=True)
    return int(candidates[0] * 3)


print(solution("12223"))
print(solution(""))
print(solution("123"))
print(solution("111999333"))
print(solution("111999"))
print(solution("1000224"))
