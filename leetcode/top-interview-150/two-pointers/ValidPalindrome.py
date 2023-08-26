# 1. 앞에서 i번째 문자와 뒤에서 i번째 문자를 "쌍으로" 비교 -> two pointers
def solution(s: str):
    new_s = []
    for c in s:
        if c.isalpha():
            new_s.append(c.lower())
        elif c.isnumeric():
            new_s.append(c)

    for i in range(len(new_s) // 2):
        left, right = new_s[i], new_s[-i - 1]
        if left != right:
            return False
    return True


def solution2(s: str):
    s = [c.lower for c in s if c.isalnum()]

    for i in range(len(s) // 2):
        left, right = s[i], s[~i]
        if left != right:
            return False
    return True


print(solution("A man, a plan, a canal: Panama"))
print(solution("race a car"))
print(solution("0P"))
print(solution(" "))
print(solution(" r"))
print(solution(""))
